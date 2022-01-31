this project will take layers and smoosh them into as many images as you want.

you give the program a bunch of layers that look like this:

![Sample](nft_project/nft/background/cyanback.png)
![Sample](nft_project/nft/eyes/commoneyes.png)
![Sample](nft_project/nft/head/yellowhead.png)
![Sample](nft_project/nft/mouth/smilemouth.png)


and it smooshes them together until you get a single image. it does this as many times as you want:
![Sample](nft_project/results/billy%20bones11.png)


current state: makes pretty pictures. has nothing to do with blockchains yet.

updates:

program now makes paths by looking into the nft folder and finding all the files.
now all images are verified as unique
you can now add weights to increase or decrease the rarity of attributes.
can calculate the rarity of attributes
can generate metadata in json format
can generate individual json files for each image
can generate a csv file with all the metadata

needs updates:
need a way to handle infinite loop by asking for more unique images than possible with the given attributes.
calculate possible combinations of attributes and warn if not enough layers for desired output
refactor code to make it more readable
refactor code to make it more efficient
refactor code to make it more modular
i might want to redo how the image paths are stored in the class so I don't need to split to get traits

if you want to try this yourself...
clone the repo:

the __main__.py file calls the make_images() function. it takes in the number of images you want to make. and stores them in the results folder.

this is a work in progress. once I feel like this program is complete, I will add instructions on how to add your own layers and generate your own images.
