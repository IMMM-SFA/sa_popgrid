import argparse
import os

from population_gravity.sensitivity import Lhs


def main(n_samples, out_directory, alpha_urban_upper=2.0, alpha_urban_lower=-2.0, alpha_rural_upper=2.0,
         alpha_rural_lower=-2.0, beta_urban_upper=2.0, beta_urban_lower=-2.0, beta_rural_upper=2.0,
         beta_rural_lower=-2.0, kernel_density_lower=50000, kernel_density_upper=100000):

    # generate latin hypercube sample
    lhs = Lhs(alpha_urban_bounds=[alpha_urban_lower, alpha_urban_upper],
              alpha_rural_bounds=[alpha_rural_lower, alpha_rural_upper],
              beta_urban_bounds=[beta_urban_lower, beta_urban_upper],
              beta_rural_bounds=[beta_rural_lower, beta_rural_upper],
              kernel_distance_meters_bounds=[kernel_density_lower, kernel_density_upper],
              n_samples=n_samples,
              problem_dict_outfile=os.path.join(out_directory, f'lhs_{n_samples}_problem_dict.p'),
              sample_outfile=os.path.join(out_directory, f'lhs_{n_samples}_sample.npy'))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('n_samples', metavar='n', type=int, help='an integer for the number of samples')
    parser.add_argument('output_directory', metavar='outdir', type=str, help='directory where the outputs will be written')

    args = parser.parse_args()

    main(args.n_samples, args.output_directory)


