# The World in a Day — Wednesday, November 18, 2026

Entry for make.fun's **news-image-20261118** bounty: sum up the world's
news of Wednesday 18 November 2026 in one image.

The image is an illustrated vintage newspaper front page (the PIL
draft in `draw_frontpage.py` set the layout and headlines), leading
with the first-ever
Xi–Trump–Putin trilateral moment at the Shenzhen APEC summit, Iran's
strikes on Gulf bases after the US hit Qeshm Island, and Ukraine's
second-day strike on the Kerch Bridge — plus briefs on Alaska's Senate
result, the DR Congo Ebola outbreak, the US losing measles-free
status, the Knesset speaker vote, the Siberia plane crash, Nvidia's
results, and Cambridge Dictionary's word of the year.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies `entry.png` (1024×1024 PNG) to the output directory
byte for byte, so repeated runs always produce identical output. No
network, no dependencies beyond the Python standard library.

## License

MIT — see `LICENSE`.
