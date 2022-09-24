wgetの使い方
wgetコマンドの引数にURLを指定すると、そのURLのコンテンツがダウンロードされファイルとして保存される。
http://gihyo.jp/のようにディレクトリ名を引数にしてするとindex.htmlという名前になる。
```bash
wget http://gihyo.jp/
```
-Oオプションでファイル名を明示的に指定できる。
```bash
wget http://gihyo.jp/ -O gihyo_top.html
```
ファイル名として-を指定すると標準出力に出力できる。
パイプで他のコマンドに渡したりできる。
進捗状況の表示を抑制する-qオプションを併用すると読みやすくなる。

よく使うオプション
| オプション                       | 説明                                                                  | 
| ------------------------------- | --------------------------------------------------------------------- | 
| -V, --version                   | Wgetのバージョンを表示する。                                          | 
| -h, --help                      | ヘルプを表示する。                                                    | 
| -q, --quite                     |  進捗状況などを表示しない。                                           | 
| -O file, --output-document=file | fileに保存する。                                                      | 
| -c, --continue                  | 前回の続きからファイルのダウンロードを再開する。                      | 
| -r, --recursive                 | リンクを辿って再起的にダウンロードする。                              | 
| -l depth                        | 再帰的にダウンロードをするときにリンクを辿る深さをdepthに制限する。   | 
| -w seconds, --wait=seconds      | 再帰的にダウンロードするときにダウンロード間隔としてseconds秒空ける。 | 
| -np, --no-parent                | 再帰的にダウンロードするときに親ディレクトリをクロールしない。        | 
| -I list, --include list         | 再起的にダウンロードするときにlistに含まれるディレクトリのみを辿る。  | 
| -N, --timestamping              | ファイルが更新されている時のみダウンロードする。                      | 
| -m, --mirror                    | ミラーリング用のオプションを有効化する。                              | 

wgetによるcrawling
--restrict-file-names=nocontrolはURLに日本語が含まれる場合に、日本語のファイル名で保存することを意味する。
```bash
wget -r --no-parent -w 1 -l 1 --restrict-file-names=nocontrol https://gihyo.jp/dp/
```
