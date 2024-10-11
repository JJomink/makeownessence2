from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
saved_poems={}
poem_initials=["ㄴ","ㄷ","ㅂ","ㅇ","ㅋ","ㅁ","ㅍ"]

def hgj(sentence):
    result = ""
    for i in range(len(sentence)):
        result += sentence[i] + "&nbsp;"  # 웹에서는 공백을 &nbsp;로 추가
    return result

def make_own_essence(poem_initial):
    poem_lines = []
    if poem_initial == "ㄴ":
        poem_lines.append(hgj(" 나                              비"))
        poem_lines.append(hgj(" 나비                          목에"))
        poem_lines.append(hgj(" 포함되는                  곤충중에"))
        poem_lines.append(hgj(" 주간에활동하     는      한무리의총칭"))
        poem_lines.append(hgj(" 이자옆집고양이이 름   이자날개를활짝펴"))
        poem_lines.append(hgj(" 고세상을자유롭게 나  는사람이라나비는"))
        poem_lines.append(hgj("              나"))
        poem_lines.append(hgj("비모양나비꼴          이아니라고해"))
        poem_lines.append(hgj("  서나비가아닐         수는없는거다"))
        poem_lines.append(hgj("   그래도이시는        진짜나비나비"))
        poem_lines.append(hgj("      제                     제"))
        poem_lines.append(hgj("       비                      비"))
        poem_lines.append(hgj("       나                        나"))
        poem_lines.append(hgj("        비                         비"))
    elif poem_initial=="ㄷ":
        poem_lines.append(hgj("              암            "))
        poem_lines.append(hgj("            암암암           "))
        poem_lines.append(hgj("          암암암암암        "))
        poem_lines.append(hgj("      암암암암암암암암암    "))
        poem_lines.append(hgj("         암암암암암암"))
        poem_lines.append(hgj("         암암암암암암"))
        poem_lines.append(hgj("         암암암암암암"))
        poem_lines.append(hgj("      암암암암암암암암암    "))
        poem_lines.append(hgj("    *   *   *   *   *   *"))
        poem_lines.append(hgj("    *   *   *   *   *   *"))
        poem_lines.append(hgj("    *   *   *   *   *   *"))
        poem_lines.append(hgj("      암암암암암암암암암    "))
        poem_lines.append(hgj("        암암암암암암암    "))
        poem_lines.append(hgj("        암암암암암암암    "))
        poem_lines.append(hgj("        암암암암암암암    "))
        poem_lines.append(hgj("      암암암암암암암암암    "))
        poem_lines.append(hgj("       암암암암암암암암    "))
        poem_lines.append(hgj("    암암암암암암암암암암암    "))
        poem_lines.append(hgj("    암암암암암암암암암암암    "))
        poem_lines.append(hgj("    암암암암암암암암암암암    "))
        poem_lines.append(hgj("    암암암암암암암암암암암    "))
        poem_lines.append(hgj("    암암암암암암암암암암암    "))
    elif poem_initial=="ㅂ":
        poem_lines.append(hgj(" 파랑                   파"))
        poem_lines.append( hgj("100964                  랑파"))
        poem_lines.append(hgj("파랑                 랑파랑"))
        poem_lines.append(hgj("  파랑             0000ff"))
        poem_lines.append(hgj("    파랑         랑파"))
        poem_lines.append(hgj("       파랑      랑파"))
        poem_lines.append(hgj("          파     파랑"))
        poem_lines.append(hgj("            랑    파랑"))
        poem_lines.append(hgj("              파     파랑"))
        poem_lines.append(hgj("                0000ff"))
        poem_lines.append(hgj("                     파랑"))
        poem_lines.append(hgj("                      aa89bd"))
        poem_lines.append(hgj("                         보라"))
        poem_lines.append(hgj("                        보라"))
        poem_lines.append(hgj("                       aa89bd"))
        poem_lines.append(hgj("                          보라"))
        poem_lines.append(hgj("                            보라"))
        poem_lines.append(hgj("                          보라"))
        poem_lines.append(hgj("                       ffffff"))
    elif poem_initial=="ㅇ":
        poem_lines.append(hgj("                 사파이                   어사파"))
        poem_lines.append(hgj("               이어사파이                  어사파"))
        poem_lines.append(hgj("             이어사  파이어                사파이"))
        poem_lines.append(hgj("           어사파      이어사              파이어"))
        poem_lines.append(hgj("         사파이          어사파            이어사"))
        poem_lines.append(hgj("       파이어              사파이          어사파"))
        poem_lines.append(hgj("     이어사                 파이어         사파이"))
        poem_lines.append(hgj("   사파이어사파이어사파이어사파이어사          파이어"))
        poem_lines.append(hgj("  사파이어사파이어사파이어사파이어사파         파이어"))
        poem_lines.append(hgj("사파이어사파               이어사파이어      사파이"))
    elif poem_initial=="ㅋ":
        poem_lines.append(hgj("                       寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("     死死死死       寫寫寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("     死死死死     寫寫寫寫寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫死死死死寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫死死寫寫寫寫寫寫死死寫寫寫寫寫         寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫死死寫寫寫寫寫寫寫寫寫寫寫寫寫         寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫死死死           寫寫寫寫寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫寫                  寫寫寫死死死死寫寫寫寫"))
        poem_lines.append(hgj("寫寫死死寫寫寫寫寫        寫寫寫        寫寫寫寫寫寫死死寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫        寫寫寫寫寫        寫寫寫寫死死寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫        寫寫寫寫寫        寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫死死死寫        寫寫寫寫寫        寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫        寫寫寫        寫寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫死死死寫寫寫                  寫寫寫寫寫寫寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫死死死死寫           寫寫死死死死死死寫寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫寫死死死死寫寫寫寫"))
        poem_lines.append(hgj("寫寫寫寫寫寫寫寫寫寫寫寫寫死死死死死寫寫寫寫寫死死死死寫寫寫寫"))
    elif poem_initial=="ㅁ":
        poem_lines.append(hgj("                톡"))
        poem_lines.append(hgj("              톡톡톡"))
        poem_lines.append(hgj("            톡  톡톡톡"))
        poem_lines.append(hgj("          톡   톡톡톡톡톡"))
        poem_lines.append(hgj("        톡톡   톡톡톡톡톡톡"))
        poem_lines.append(hgj("       톡톡   알이깨지는소리"))
        poem_lines.append(hgj("      톡톡   눈물을떨구는소리"))
        poem_lines.append(hgj("      톡톡   나를두드리는소리"))
        poem_lines.append(hgj("      톡톡   한결같은마음소리"))
        poem_lines.append(hgj("       톡톡톡톡톡톡톡톡톡톡"))
        poem_lines.append(hgj("         톡   톡톡톡톡톡톡"))
        poem_lines.append(hgj("           톡톡톡톡톡톡"))
    elif poem_initial=="ㅍ":
        poem_lines.append(hgj("열      드드드드    리리리리      미       피피피피    슬슬슬슬   손을가장      시"))
        poem_lines.append(hgj("쇠      드드드드    리리리리      미       피피피피    슬슬슬슬   헛딛었던      시"))
        poem_lines.append(hgj("구      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("멍      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("위      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("의      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도 도 도 도 레 레 레 레 미 미 미 미 파 파 파 파 솔 솔 솔 솔 라 라 라 라 시 시 시 시"))
    elif poem_initial in saved_poems:
        poem_lines.extend(saved_poems[poem_initial])
        
    return poem_lines
@app.route("/", methods=["GET", "POST"])
def home():
    poem_lines = []
    poem_name = ""
    show_memo = False

    if request.method == 'POST':
        poem_initial = request.form.get('poem_initial')
        if poem_initial not in poem_initials:  # 등록된 초성 확인
            show_memo = True  # 메모장 표시
        else:
            poem_lines = make_own_essence(poem_initial)
            if not poem_lines:
                show_memo=True
            poem_name = {
                "ㄴ": "나비",
                "ㄷ": "등대",
                "ㅂ": "번개",
                "ㅇ": "알루미늄",
                "ㅋ": "카메라",
                "ㅁ": "물방울",
                "ㅍ": "피아노"
            }.get(poem_initial, "알 수 없는 초성")
        
            
    return render_template('index.html', poem_lines=poem_lines, poem_name=poem_name, show_memo=show_memo)
@app.route("/save_poem", methods=["POST"])
def save_poem():
    data = request.get_json()
    poem_initial = data['poem_initial']
    new_poem = data['new_poem']
    if poem_initial in saved_poems:
        saved_poems[poem_initial].append(new_poem)
    else:
        saved_poems[poem_initial] = [new_poem]

    return jsonify({"status": "success", "message": f"새로운 시가 추가되었습니다: {poem_initial}"})


    

if __name__ == "__main__":
    app.run(debug=True)
