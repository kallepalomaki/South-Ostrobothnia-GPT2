# South-Ostrobotnia-GPT2
Experiments with GPT2: Finetuning a Finnish GPT2 to South Ostrobothnia

This is a not so serious attempt to make a GPT2 based text generator of South Ostrobothnian dialect.

GPT2 base model I'm using is this: https://huggingface.co/Finnish-NLP/gpt2-finnish?text=Teksti%C3%A4+tuottava+teko%C3%A4ly+on
version Finnish-NLP/gpt2-finnish by Aapo Tanskanen and Rasmus Toivanen

I have ran GPT2 Finetuning script SouthOstrobotniaGPT2.ipynb in Google Colab. 

Colab notebook is based (with small number of edits) on the following tutorial:
https://colab.research.google.com/drive/13dZVYEOMhXhkXWfvSMVM1TTtUDrT6Aeh#scrollTo=0NmMdkZO8R6q

For generation of South Ostrobotnian dialect some model adaptation material is needed.
I have crawled some texts from the following blogs: http://pohopekka.blogspot.com/, https://www.blogit.fi/tag/pakina

You can run the crawler by the shell script run_crawl.sh. I have ran the crawler locally thus it is not part of
Colab notbook.

Running the crawler scripts requires following installations:
virtualenv --python python3 venv
venv/bin/pip install bs4 requests

Currently used python packages are listed in
requirements.txt

The crawled texts will be placed in ep.txt. You'll need to copy ep.txt to the same google drive directory
where you run the Colab-script.


