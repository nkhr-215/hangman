def hangman(word):
    wrong = 0 #間違えた回数を数える
    stages = ["",
             "________        ",
             "|               ",
             "|       |       ",
             "|       0       ",
             "|      /|       ",
             "|      /        ",
             "|               "
             ] #ステージ
    rletters = list(word) #wordをリスト化
    board = ["_"] * len(word) #_*文字数
    win = False #まだ誰も勝ってないから
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1: #8-1より間違えた回数が小さいなら繰り返す
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg) #文字を打たせる
        if char in rletters: #boardを更新
            cind = rletters.index(char) #rlttersの中のcharが割り当てられた番を取り出す
            board[cind] = char #boardのcind番にcharを入れる
            rletters[cind] = '$' #かぶり文字対策
        else:
            wrong += 1 #不正解なら数える
            
        print(" ".join(board)) #スコアボード,更新されたboardを改行せず出力
        e = wrong + 1
        print("\n".join(stages[0:e])) #0～eまで改行して出力
        
        if "_" not in board: #boardから_がなくなったら
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break            
    if not win: #whileし終わってwin=Falseなら
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))
               
hangman("cat")
