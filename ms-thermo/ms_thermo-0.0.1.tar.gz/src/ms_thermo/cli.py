#!/usr/bin/env python
"""
cli.py

Command line interface for tools in ms_thermo
"""

import click
from ms_thermo.tadia import tadia_table, tadia_cantera
from ms_thermo.yk_from_phi import yk_from_phi
from ms_thermo.fresh_gas import fresh_gas
from pkg_resources import resource_listdir, resource_string

@click.command()
@click.argument('temperature', nargs=1)
@click.argument('pressure', nargs=1)
@click.argument('phi', nargs=1)
def tadia_table_cli(temperature, pressure, phi):
	"""Calculate the adiabatic flame temperature of a kero-air mixture from 2S_KERO_BFER table"""
	burnt_temperature, yk = tadia_table(float(temperature), float(pressure), float(phi))
	print(f"\nThe adiabatic flame temperature of a mix C10H22-air from tables is : {burnt_temperature:.2f} K.")
	print("\nSpecies     |    Mass fraction")
	print("------------------------------")
	for specie in yk.keys():
		print(f'{specie:12s}|       {yk[specie]:.3f}')

@click.command()
@click.argument('temperature', nargs=1)
@click.argument('pressure', nargs=1)
@click.argument('phi', nargs=1)
@click.argument('fuel', nargs=1)
@click.argument('path2cti', nargs=1)
def tadia_cantera_cli(temperature, pressure, phi, fuel, path2cti):
	"""Calculate the adiabatic flame temperature of a fuel-air mixture from cantera"""
	burnt_temperature, yk = tadia_cantera(float(temperature), float(pressure), float(phi),
		str(fuel),str(path2cti))
	print(f"\nThe adiabatic flame temperature of a mix C10H22-air from cantera is : {burnt_temperature:.2f} K.")
	print("\nSpecies     |    Mass fraction")
	print("------------------------------")
	nb_other_species = 0
	y_other_species = 0
	for specie in yk.keys():
		if yk[specie] < 1e-3:
			nb_other_species +=1
			y_other_species += yk[specie]
		else:
			print(f'{specie:12s}|       {yk[specie]:.3f}')
	print(f'+ {nb_other_species} others |       {y_other_species:.3f}')

@click.command()
@click.argument('c_x', nargs=1)
@click.argument('h_y', nargs=1)
@click.argument('phi', nargs=1)
def yk_from_phi_cli(c_x, h_y, phi):
	"""Calculate the mass fractions of a fuel-air mixture"""
	yk = yk_from_phi(float(c_x), float(h_y), float(phi))
	print("\nSpecies     |    Mass fraction")
	print("------------------------------")
	for specie in yk.keys():
		print(f'{specie:12s}|       {yk[specie]:.3f}')


@click.command()
@click.argument('temperature', nargs=1, type=float)
@click.argument('pressure', nargs=1, type=float)
@click.argument('phi', nargs=1, type=float)
def fresh_gas_cli(temperature, pressure, phi):
	"""Calculate the conservative variables of a kero-air mixture"""
	rho,rhoE,rhoyk = fresh_gas(temperature, pressure, phi)
	print(f'\nrho       |  {rho:.3f} kg/m3')
	print(f'rhoE      |  {rhoE:.3f} J.kg/m3')
	print(f'rhoYk     |')            
	for specie in rhoyk.keys():
		print(f' {specie:9s}|  {rhoyk[specie]:.3f} mol.kg/m3')
