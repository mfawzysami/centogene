#!/usr/bin/env python
import os, sys
import csv
from typing import Tuple
from collections import defaultdict , Counter
from argparse import ArgumentParser


def prepare_parser():
    """
     Prepare parser command line arguments
    """
    p = ArgumentParser(description="Combining Variants with Disease Table")
    p.add_argument("--variants", "-i", help="Absolute path of your variants Text File", default=None, required=True)
    p.add_argument("--diseases", "-d", help="The absolute path of your diseases CSV File", default=None, required=True)
    p.add_argument("--out", "-o",
                   help="The absolute path of the combined output CSV file. Optional , Defaults: ./output.results.csv",
                   required=False, default="./output.results.csv")

    return p


def prepare_variants(variants_file: str) -> Tuple[defaultdict,Counter]:
    """
    This function will take the variants file, process it, and return a tuple of results
    """
    if variants_file is None or len(variants_file) == 0:
        raise Exception("Variants file is required")
    if not os.path.exists(variants_file):
        raise Exception("Variants file does not exist. Please make sure the variant file does exist and try again")
    variants = defaultdict(dict)
    with open(variants_file, "r") as reader:
        contents = reader.readlines()
        # Cosmetics
        contents = [x.replace("\n", "") for x in contents]
        # get rid of headers
        lines = contents[1:]
        # Preprocessing
        data = [line.strip().split("\t") for line in lines if len(line) > 1]
        variant_types = []
        for variant_id, chrom, vartype, vcf_pos, vcf_ref, vcf_alt in data:
            variants[variant_id.strip()] = {
                "chrom": chrom,
                "vartype": vartype,
                "vcf_pos": vcf_pos,
                "vcf_ref": vcf_ref,
                "vcf_alt": vcf_alt
            }
            variant_types.append(vartype)
        stats = Counter(variant_types)
    return variants , stats


def prepare_diseases(diseases_file: str) -> defaultdict:
    """
    This function will process the diseases table and return a dictionary
    """
    if diseases_file is None or len(diseases_file) == 0:
        raise Exception("Disease file must be set")
    if not os.path.exists(diseases_file):
        raise Exception("Disease file should exist")
    diseases = defaultdict(dict)
    with open(diseases_file,"r",encoding="utf-8-sig") as file:
        reader = csv.reader(file,quotechar='"',delimiter=',')
        contents = [line for line in reader]
        lines = [line for line in contents if not line[0].startswith("#")]
        for variant_id, gene, disease, mutationtype, acc_num, n_pub in lines:
            diseases[variant_id.strip()] = {
                "gene": gene,
                "disease": f"\"{disease}\"",
                "mutationtype": mutationtype,
                "acc_num": acc_num,
                "n_pub": n_pub
            }
    return diseases


def combine(output_file: str, variants: defaultdict,variants_stats:Counter, diseases: defaultdict) -> bool:
    """
    This function will combine both processed files: variants and diseases....
    """
    if output_file is None or len(output_file) == 0:
        raise Exception("Output file should be set")
    if len(diseases.keys()) < 1:
        raise Exception("Diseases dictionary should not be empty")
    get_coordinate = lambda attr: f"{attr['chrom']}-{attr['vcf_pos']}-{attr['vcf_ref']}-{attr['vcf_alt']}"
    get_mutation_variant_type = lambda var_attrs, dis_attrs: f"{dis_attrs['mutationtype']}-{var_attrs['vartype']}"
    var_mutation_types = []
    with open(output_file, "w") as outfile:
        writer = csv.writer(outfile,delimiter=',',quotechar='"',lineterminator='\n')
        keys = list(diseases.keys())
        vkeys = list(variants.keys())
        variants_values_len = len(variants[vkeys[0]].keys())
        headers = ["variant_id"] + list(variants[vkeys[0]].keys()) +list(diseases[keys[0]].keys())
        # add the additional column attribute
        # <chrom>-<vcf_pos>-<vcf_ref>-<vcf_alt>
        headers.extend(["Mutation_Count","Coordinate","MutationType_VarType","MutationType_VarType_Count"])
        # write out headers first
        writer.writerow(headers)
        rows = []
        for variant_id, attrs in diseases.items():
            # since, we need to combine the data INTO diseases
            # diseases object will be the modifier
            if not variant_id in variants:
                print(f"{variant_id} does not found in variants")
                line = [variant_id] + ["N/A" for x in range(variants_values_len)] + list(attrs.values()) \
                + ["N/A","N/A","N/A"]
            else:
                variant_details = variants[variant_id]
                coordinate = get_coordinate(variant_details)
                variant_mutation_type = get_mutation_variant_type(variants[variant_id], attrs)
                var_mutation_types.append(variant_mutation_type)
                line = [variant_id] + list(variant_details.values()) + list(attrs.values())
                trailing_attrs = [variants_stats[variant_details['vartype']],coordinate,f"{attrs['mutationtype']}-{variant_details['vartype']}"]
                line.extend(trailing_attrs)
            #writer.writerow(line)
            rows.append(line)
        mutationType_varType_stats = Counter(var_mutation_types)
        rows = [row + [mutationType_varType_stats[row[-1]]] for row in rows]
        for row in rows:
            writer.writerow(row)

    return True


def main():
    """
    The main entry point of the program
    :return: None
    """
    p = prepare_parser()
    args = p.parse_args()
    if len(sys.argv) < 2:
        return p.print_help()
    try:
        variants , stats = prepare_variants(args.variants)
        diseases = prepare_diseases(args.diseases)
        if combine(args.out, variants,stats, diseases):
            print("All Done.")
        else:
            print("There is an error")

    except Exception as e:
        p.error(str(e))
        return p.print_help()


# Main Entry Point of the program
if __name__ == '__main__':
    main()
