import argparse

if __name__ == '__main__':
    # Get arguments.
    parser = argparse.ArgumentParser(description='Downlader')
    parser.add_argument('query', type=str, help='Your search query')
    parser.add_argument('-s', '--site', type=str, help='Where you want to download from')
    args = parser.parse_args()
    # Handle arguments.
    if args.site is None:
        print('parsing through all sites')
    elif args.site == 'animeout':
        from animeout import animeoutDL
        animeoutdl = animeoutDL(args.query)
    elif args.site == 'kissmanga':
        from kissmanga import kissmangaDL
        kissmangadl = kissmangaDL(args.query)
    elif args.site == 'igggames':
        from igggames import igggamesDL
        igggamesdl = igggamesDL(args.query)

