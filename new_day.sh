#!/bin/bash

COOKIE_FILE="cookie.txt"

# create new directory for the day and replace input path in file
DAY_PADDED=$(date +%d)
DIR="day_$DAY_PADDED"
cp -r "day_xx" "$DIR"
sed -i '' "s/day_xx/$DIR/g" "$DIR/main.py"

# fetch in put and save to input.txt
COOKIE="$(< "$COOKIE_FILE" tr -d '\n')"
YEAR=$(date +%Y)
DAY=$(date +%-d)
INPUT_URL="https://adventofcode.com/$YEAR/day/$DAY/input"
TEMP_INPUT="temp-input.txt"
curl "${INPUT_URL}" --compressed \
  -H "Cookie: session=${COOKIE}" \
  -o "${TEMP_INPUT}"

cp ${TEMP_INPUT} "$DIR"/input.txt
rm ${TEMP_INPUT}
