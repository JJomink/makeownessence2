from flask import Flask, render_template, request
import random

app = Flask(__name__)

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
        poem_lines.append(hgj("       톡톡   톡톡톡톡톡톡톡"))
        poem_lines.append(hgj("      톡톡   톡톡톡톡톡톡톡톡"))
        poem_lines.append(hgj("      톡톡   톡톡톡톡톡톡톡톡"))
        poem_lines.append(hgj("      톡톡   톡톡톡톡톡톡톡톡"))
        poem_lines.append(hgj("       톡톡톡톡톡톡톡톡톡톡"))
        poem_lines.append(hgj("         톡   톡톡톡톡톡톡"))
        poem_lines.append(hgj("           톡톡톡톡톡톡"))
    elif poem_initial=="ㅍ":
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도      드드드드    리리리리      미       피피피피    슬슬슬슬   비비비비      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도         도          레        미         파          솔         라      시"))
        poem_lines.append(hgj("도 도 도 도 레 레 레 레 미 미 미 미 파 파 파 파 솔 솔 솔 솔 라 라 라 라 시 시 시 시"))
        
        
        

    return poem_lines

@app.route("/",methods=["GET","POST"])
def home():
    poem_lines = []
    poem_name=""
    if request.method == 'POST':
        poem_initial = request.form.get('poem_initial')
        poem_lines = make_own_essence(poem_initial)
        
        if poem_initial == "ㄴ":
            poem_name = "나비"
        elif poem_initial == "ㄷ":
            poem_name = "등대"
        elif poem_initial == "ㅂ":
            poem_name = "번개"
        elif poem_initial == "ㅇ":
            poem_name = "알루미늄"
        elif poem_initial == "ㅋ":
            poem_name = "카메라"
        elif poem_initial == "ㅁ":
            poem_name = "물방울"
        elif poem_initial == "ㅍ":
            poem_name = "피아노"
            
    return render_template('index.html', poem_lines=poem_lines,poem_name=poem_name)


if __name__ == "__main__":
    app.run(debug=True)
