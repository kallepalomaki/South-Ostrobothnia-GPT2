# South-Ostrobotnia-GPT2
Experiments with GPT2: Finetuning a Finnish GPT2 to South Ostrobotnia

This is a not so serious attempt to make GPT2 based generator of South Ostrobotian dialect.

GPT2 base model I'm using is this: https://huggingface.co/Finnish-NLP/gpt2-finnish?text=Teksti%C3%A4+tuottava+teko%C3%A4ly+on
version Finnish-NLP/gpt2-finnish by Aapo Tanskanen and Rasmus Toivanen

Colab notebook is based (with small number of edits) on the following tutorial:
https://colab.research.google.com/drive/13dZVYEOMhXhkXWfvSMVM1TTtUDrT6Aeh#scrollTo=0NmMdkZO8R6q

Adaptation material is crawled from the following blogs: http://pohopekka.blogspot.com/, https://www.blogit.fi/tag/pakina

You can run the crawler by the shell script run_crawl.sh
The crawled texts will be placed in ep.txt

I have ran GPT2 Finetuning script SouthOstrobotniaGPT2.ipynb in Google Colab. You should transfer texts-file ep.txt to
same directory where you run Colab-notebook
