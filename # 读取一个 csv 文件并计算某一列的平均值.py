#!/usr/bin/env python3
import pandas as pd

def main():
	try:
		df = pd.read_csv('data.csv')
		avg = df['value'].mean()
		print(avg)
	except Exception as e:
		print('Error:', e)

if __name__ == '__main__':
	main()