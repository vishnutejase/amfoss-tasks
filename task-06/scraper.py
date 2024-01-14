from bs4 import BeautifulSoup
import requests
import re
import csv

def find_scores():
    source = requests.get("https://www.espncricinfo.com/live-cricket-score").text

    soup = BeautifulSoup(source,"lxml")
    scores = soup.find_all('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')

    with open("scores.csv", "w") as scores_file:
        None

    count = 0
    msg_1 = ""
    msg_2 = ""

    for i in range(len(scores)):
        input_string = str(scores[i])

        match_title_pattern = re.compile(r'title="(.*?)"')
        span_content_pattern = re.compile(r'<span>(.*?)<\/span>')

        title_match = match_title_pattern.search(input_string)
        span_content_match = span_content_pattern.search(input_string)

        title_string = title_match.group(1) if title_match else None
        span_content_string = re.sub('<[^>]*>', '', span_content_match.group(1)) if span_content_match else None

        with open("scores.csv","a") as scores_file:
            cw = csv.writer(scores_file)
            # cw.writerow([title_string,span_content_string])
            if count < len(scores)/2:
                if title_string == span_content_string:
                    msg_1 += f"```{title_string}```"
                    cw.writerow([title_string])
                else:
                    msg_1 += f"```{title_string}\n{span_content_string}```"
                    cw.writerow([title_string, span_content_string])
            else:
                if title_string == span_content_string:
                    msg_2 += f"```{title_string}```"
                    cw.writerow([title_string])
                else:
                    msg_2 += f"```{title_string}\n{span_content_string}```"
                    cw.writerow([title_string, span_content_string])

        count += 1
    return msg_1,msg_2