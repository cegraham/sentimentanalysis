"""This script takes as input disentangled xml chat files and creates a csv. It groups conversations by conversation
ids and concatenates consecutive utterances from same speaker in a conversation (adds semicolon between concatenated
utterances) """

import sys, os, csv
import xml.etree.ElementTree as ET
from datetime import datetime

JOIN_THRESHOLD = 100000000  # seconds
walkdir = "/Users/kushp/Documents/preethac-Software-related-Slack-Chats-with-Disentangled-Conversations-77bcdcf 2/data/pythondev/2017"

def join_messages_in_file(filename):
    chat = []
    prev_time = JOIN_THRESHOLD * -100
    prev_speaker = ""
    prev_conv_id = -1

    with open(filename, 'r') as f:
        tree = ET.parse(filename)

        # for node in tree.findall('message'):
        #     conv_id = node.get('conversation_id')
        #     if conv_id not in convs:
        #         convs.append(conv_id)

        # for conv in convs:
        for node in tree.findall('message'):
            conv_id = node.get('conversation_id')
            timestamp = datetime.strptime((node.find('ts').text), "%Y-%m-%dT%H:%M:%S.%f").timestamp()
            speaker = node.find('user').text
            message = str(node.find('text').text)
            #print (timestamp, speaker, message)
            if (timestamp - prev_time) < JOIN_THRESHOLD and speaker == prev_speaker and conv_id == prev_conv_id:
                line = message.replace(r'\r\n', '')
                chat[-1][3] = chat[-1][3] + "; " + line
            else:
                line = [conv_id, str(timestamp), speaker, message.replace(r'\r\n', '')]
                chat.append(line)

            prev_time = timestamp
            prev_speaker = speaker
            prev_conv_id = conv_id

    return chat


if __name__ == "__main__":

    for root, dirnames, filenames in os.walk(walkdir):
        for filename in filenames:
            if not filename.endswith('.xml'):
                continue
            else:
                path = os.path.join(root, filename)
                print (path)

                chatFileName = path
                outfile = os.path.join(str(path[:-4]) + '-concat-group' + '.csv')

                with open(outfile, 'w', encoding='utf-8-sig') as fpointer:
                    joined_chat = join_messages_in_file(chatFileName)
                    csv_writer = csv.writer(fpointer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(['speaker','message'])
                    for msg in joined_chat:
                        csv_writer.writerow(msg)