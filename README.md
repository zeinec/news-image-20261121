[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/zeinec/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/zeinec/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# GLOBAL HERALD — Saturday, 21 November 2026

Built for the [make.fun news-image-20261121 bounty](https://make.fun/bounty/news-image-20261121): one image that sums up the world's
news of Saturday 21 November 2026. A one-page vintage newspaper in full
colour — masthead, lead story, a pinned world map, and six more stories.

## The image

`entry.png` (1024×1024, ~120 KB) is drawn programmatically from scratch
(`work/render.py`, Pillow + real fonts) — every letter is real text, so
nothing is garbled at any size, and the page stays legible at ~300 px wide:
the masthead, the date, the lead headline and the map pins all still read.

Layout, top to bottom:

- **Masthead** — GLOBAL HERALD, Saturday, 21 November 2026.
- **Lead: EARTH SHAKES PERU** — magnitude 6.8 quake in Junín, tremors felt
  320 km away in Lima, with a flat-colour Andes panel and an M 6.8 badge.
- **THE WORLD TODAY** — a simplified world map with the lead story starred
  in Peru and stories 1, 2, 4, 5 pinned in Beijing, Odisha, New York and
  Wellington.
- **Six story cards** — summit, cyclone, markets, Rikers, cricket, Nepal.

## The day's stories (as first reported 21 November 2026)

1. **Peru earthquake** — magnitude 6.8 strikes Junín, central Peru;
   tremors felt in Lima, ~320 km away.
2. **Trump–Xi–Putin summit** — pledges but no breakthroughs; Trump to
   address Americans after the historic talks.
3. **Cyclone Akvan** — makes landfall on the Odisha coast with strong winds
   and heavy rain.
4. **NSE goes fifth** — India's National Stock Exchange becomes the world's
   5th-largest listed exchange; record foreign inflows into Indian shares.
5. **Rikers to close 2032** — New York City mayor sets a new date to shut
   the Rikers Island jail complex.
6. **KL Rahul makes history** — a century in Wellington, the first Indian
   opener with Test centuries in all four SENA countries.
7. **Nepal PM to Delhi** — Balendra Shah's first foreign trip, India,
   22–23 November.

## Why this shape

Past winners in this family won with one bold concept that fills the frame —
a world map (news-image-01, and the map-front-page entries that topped the
leaderboard). This entry keeps the newspaper the reader asked for, but adds
the map band so the day's geography is visible at a glance, and keeps the
story count low so each headline stays big enough to read.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) checks the PNG signature and the
1 MiB cap, then copies `entry.png` to the output directory. It is
deterministic: two runs write identical bytes.

## License

MIT — see `LICENSE`.
