import argparse
import requests
import html2text

# 引数パーサを作成
parser = argparse.ArgumentParser(description='URLのHTMLをMarkdownに変換します')
parser.add_argument('url', help='HTMLのURL')
parser.add_argument('output_file', help='出力Markdown')

# 引数を解析
args = parser.parse_args()

# URLからHTMLを取得
try:
    response = requests.get(args.url)
    response.raise_for_status()  # HTTPエラーを確認
    html_source = response.text
except requests.exceptions.RequestException as e:
    print(f'URLの取得に失敗しました: {e}')
    exit(1)

# html2textインスタンスを作成
converter = html2text.HTML2Text()

# HTMLをMarkdownに変換
markdown_text = converter.handle(html_source)

# Markdownテキストを指定された出力ファイルに書き込む
with open(args.output_file, 'w', encoding='utf-8') as f:
    f.write(markdown_text)