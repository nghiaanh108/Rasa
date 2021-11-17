# Rasa
create folder name 

1. downloaded:
 - bpe: vi.wiki.bpe.vs200000.d300.w2v.bin, vi.wiki.bpe.vs200000.model -> link download: "https://fasttext.cc/docs/en/crawl-vectors.html"
 - fasttext: cc.vi.300.bin, cc.vi.300.vec -> link download: "https://fasttext.cc/docs/en/crawl-vectors.html"
		


2.model:
- cmd line "rasa train"
- run: "rasa shell"

- rasa run -m models --enable-api --cors "*" --debug
- uvicorn main:app --reload
- rasa run actions


- rasa run --endpoints endpoints.yml --credentials credentials.yml

- ngrok http 5005
