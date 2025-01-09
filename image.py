from PIL import Image, ImageDraw, ImageFont

# 試合情報を管理するクラス
class match:
    # クラスのプロパティを初期化（デフォルト値を空文字列に設定）
    date = ""         # 試合日
    category = ""     # 節
    victory = ""      # 勝利チーム 
    hometeam = ""     # ホームチーム名
    awayteam = ""     # アウェイチーム名
    scoreDetail = ""  # 試合のスコア詳細（例: 2-1）
    venue = ""        # 試合会場（例: 東京ドーム）

    # コンストラクタ：初期化時に試合情報を設定
    def __init__(self, date, category, victory, hometeam, awayteam, scoreDetail, venue):
        self.date = date
        self.category = category
        self.victory = victory
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.scoreDetail = scoreDetail
        self.venue = venue

    # 試合情報をコンソールに出力するメソッド
    def show_match(self):
        print(self.date, self.category, self.victory, self.hometeam, self.awayteam, self.scoreDetail, self.venue)

# 試合情報をもとに画像を生成する関数
    def make_image(self):
        # 画像の幅と高さを指定
        img_width = 800   # 画像の幅（ピクセル）
        img_height = 400  # 画像の高さ（ピクセル）
        background_color = (255, 241, 0)  # 画像の背景色（白）

        # Pillowを使用して新しい画像を作成
        image = Image.new("RGB", (img_width, img_height), color=background_color)  # RGB形式の白い画像
        draw = ImageDraw.Draw(image)  # 描画オブジェクトを作成

        # フォントの設定
        try:
            # 日本語対応のフォントを指定
            font = ImageFont.truetype("NotoSansJP-Bold.ttf", 28)  # フォントサイズ20
        except IOError:
            # フォントが見つからない場合はデフォルトフォントを使用
            font = ImageFont.load_default()

        scoreDetail = self.scoreDetail.replace(" ","")
        # 試合日を画像の中央上部に描画
        self.make_text(draw,400,20,f"J1リーグ {self.category[2:]} {self.date}",)
        self.make_text(draw,155,90,self.hometeam)
        self.make_text(draw,600,90,self.awayteam)
        self.make_text(draw,345,160,self.venue)
        self.make_text(draw,160,280,"１")
        self.make_text(draw,390,260,scoreDetail[1])
        self.make_text(draw,620,280,scoreDetail[2])
        
        # 画像を保存するファイル名を設定（カテゴリーに基づく命名）
        output_file = f"soccer_{self.category}.png"
        image.save(output_file)  # 画像を保存
        print(f"画像を保存しました: {output_file}")  # 保存完了メッセージを表示

    def make_text(self,draw,x,y,text):
        font = ImageFont.truetype("NotoSansJP-Bold.ttf", 28)  
        text_width = draw.textlength(text, font=font)
        text_height = 28

        # 中心に配置するための調整
        x -=  text_width // 2
        y -=  text_height // 2
        print(f"{text},{x},{y}")

        draw.text((x,y),text,fill=(0, 0, 0),font=font,anchor="mm")
        bbox = draw.textbbox((x, y), text, font=font) # 文字を描画  
        draw.rectangle(bbox, outline="red", width=2)
