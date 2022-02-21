docker build -t tretikoffhw2 . &&
docker run --name tretikoffhw2 tretikoffhw2 &&
docker cp tretikoffhw2:/proj/artifacts/table.pdf artifacts/table.pdf &&
docker cp tretikoffhw2:/proj/artifacts/table.tex artifacts/table.tex &&
docker rm tretikoffhw2
