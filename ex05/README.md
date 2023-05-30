# Air-hockey

<p align="center">
<img alt="air-hockey" title="JSON-Markd" src="https://raw.githubusercontent.com/mkfeuhrer/Air-hockey/master/airhockey.png" width="550" />
</p>

Simple pygame implementation of 2 player Air Hockey game. It has score updation and basic air hockey features.

## Requirements

- python 2.x or 3.x must be installed for playing. Keep all the files in same folder for proper functioning.

## Instructions 

- Player 1 - W,A,S,D
- Player 2 - arrow keys
- Player controls tha mallets disc as soon as hits either goal , score is accounted and disc is reset at center. 

## Contribute

Feel free to contribute. Add new features or improve existing codebase.

Fork and make a PR :)

Star and share the library with your community.

<a href="https://www.buymeacoffee.com/chHAzigTb" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Author

- [Mohit Khare](https://mohitkhare.me)
# ゲーム のタイトル
エアホッケー
## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
１つのPCで2つのスマッシャーを動かし、２人で対戦ができるゲーム

## ゲームの実装
###共通基本機能
* エアホッケーのフィールドに関するクラス
* エアホッケーのマレットに関するクラス
* エアホッケーのパックに関するクラス
* ゴールの後はディスクが中央から右下に向かって発射

### 担当追加機能
* マレットに当たるごとに速度変化
* 10点先取で勝利画面の表示
* ５点差がついたとき、同点になるまで負けているほうのマレット　が大きくなる
* 合計得点が5点追加されるごと障害物追加
* お互いの得点差に合わせてゴールの大きさの変化
* ゴールの後ディスクの発射方向をランダムにする
### ToDo
