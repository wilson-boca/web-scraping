import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


class GenerateWordCloud(object):
    def __init__(self):
        self.df = None
        self.stopwords = ["do", "da", "dos", "das", "meu", "seu", "nosso", "em", "você", "de", "ao", "os",
                          "no", "na", "nos", "nas", "não", "que", "quem", "mas", "são", "e", "é", "mais",
                          "muito", "um", "está", "com", "tem", "sem", "esse", "só", "nesse", "nessa", "nessas",
                          "nesses", "nestes", "neste", "outro", "outra", "pode", "este", "ficar", "sair", "para",
                          "pra", "um", "uma", "uns", "umas", "ir", "vir", "mesmo", "eu", "ser", "estar", "além",
                          "pelo", "pela", "ele", "ela", "eles", "elas", "nossa", "nossas", "nosso", "nossos", "até",
                          "fui", "foi", "fica", "ainda", "quer", "tudo", "por", "já", "porém", "lá", "la", "todos",
                          "todo", "alguma", "etc"]

    def read_csv(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def generate_image(self, image_path):
        summary = self.df.dropna(subset=['comment_body'], axis=0)['comment_body']
        all_summary = " ".join(s for s in summary)
        stopwords = set(STOPWORDS)
        stopwords.update(self.stopwords)
        wordcloud = WordCloud(stopwords=stopwords,
                              background_color="black",
                              width=1280, height=640).generate(all_summary)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.set_axis_off()
        plt.imshow(wordcloud)
        wordcloud.to_file(image_path)


if __name__ == "__main__":
    words = GenerateWordCloud()
    words.read_csv('/home/rodrigo/projects/web-scraping/tripadvisor/tripadvisor/tripadvisor.csv')
    words.generate_image('tripadvisor_word_cloud.png')
