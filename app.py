#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from random import randint
from flask_cors import CORS
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
# -*- coding: utf-8 -*- 


def randomLine(line):
  return line[randint(0, len(line)-1)]

userNumber = 0
company = ['넥슨게임즈', '넷마블', '요스타', 'X.D 글로벌']
gameName = ['블루아카이브', '페이트 그랜드 오더', '명일방주', '소녀전선']
# chooseNum = randint(0,3)

# try: 
#     chooseNum = int(chooseNum)
# except:
#     chooseNum = randint(0,3)
# else:
#     if chooseNum > 4:
#         chooseNum = randint(0,3)
#     userNumber = chooseNum-1

infoYear = randint(2014,2022)
title = (
f"게임 '{gameName[userNumber]}'의 리소스 수정ㆍ연령등급 상향 권고 관련 심의과정에 관해 조속한 정보공개를 청구 합니다.",
"대한민국 게임물관리위원회의 게임물이용등급판정 관련 행정운영에 대한 고충 민원",
"한국 게임물등급조정위원회의 게임물 이용 등급판정에 대한 민원",
"최근 대한민국 게임물관리위원회의 졸속 행정(등급상향)에 대한 민원",
f"근래 모바일게임 {gameName[userNumber]}의 연령등급 상향 행정에 관한 이의제기",
f"핸드폰 게임 「{gameName[userNumber]}」의 게임물이용 연령등급 재심의와 등급변경에 관해",
f"핸드폰 게임 `{gameName[userNumber]}`에 관한 이용자 연령등급에 관한 재심의 및 등급변경에 이의 송달합니다.",
f"모바일게임 '{gameName[userNumber]}'의 유저로서 관련 연령등급 상향 변경의 행정에 불복을 표명합니다.",
f"게임 〈{gameName[userNumber]}〉에 대한 게임물관리위원회의 졸속 행정에 반대합니다.",
f'국내 게임 "{gameName[userNumber]}"에 대한 게임물관리위원회의 결과 처리에 대한 정보공개를 촉구합니다.',
'현재 게임물관리위원회는 제대로 일을 하고 있는지 의심스럽습니다',
'게임물관리위원회의 이번 게임물이용등급 재조정 조치를 강력 반대합니다.',
'게임물이용등급 재조정에 대한 반대 민원건',
f'스마트폰 게임 {gameName[userNumber]}의 게임물이용등급 재조정을 반대합니다.',
'게임물관리위원회의 게임물이용등급 상향조치를 강력 반대합니다.',
'게임물관리위원회의 졸속행정 시정에 관한 청원',
'손바닥 뒤집듯이 바뀌는 게임물의 이용등급변경, 이대로 괜찮은겁니까?',
'게임물관리위원회의 게임물 이용등급 재조정에 강력하게 반대합니다.',
'게임물관리위원회는 제대로 된 게임의 관리를 하고 있는지 의심이 듭니다.',
'현재 일부 게임물의 심의등급 상향에 강력반대합니다.',
'게임물관리위원회의 이용등급 재조정은 심각하게 잘못되었다고 생각하며 강력반대합니다.',
'게임물관리위원회의 잘못된 게임물 등급 분류에 관한 청원',
'게임물관리위원회의 비정상적 등급 분류에 관한 건',
'게임물관리위원회의 편파적 게임물 등급 분류 행태를 제보합니다.',
'게임물관리위원회가 일을 규정대로 처리하지 않습니다.',
'게임물관리위원회가 규정대로 행정처리를 하지 않고 있습니다.',
'현재 게임물관리위원회의 행정처리가 제대로 되고 있질 않습니다.',
'현재 게임물관리위원회의 행정처리가 비상식적이라고 생각합니다.',
'게임물관리위원회가 규정처리를 제대로 하고 있지 않습니다.'
)

greeting = (
"귀 부처의 무탈한 운영을 기원합니다.",
"귀 부서의 공정한 활동을 기원합니다.",
"귀하 부처의 공정하고 적극적인 행정업무를 부탁드립니다.",
f"{gameName[userNumber]}의 민원처리&민원분류담당 공무원님 안녕하십니까.",
"겨울로의 환절기간 건강에 안녕하십니까. 민원 처리에 항상 고생 많으십니다.",
"귀 부처의 무궁한 발전을 기원합니다."
)

now = (
f'현재 귀 위원회는 플레이스토어(구글코리아 LLC. 운영), 앱스토어(애플코리아 LLC. 운영),원스토어(원스토어 LLC. 운영)플랫폼을 통해 {company[userNumber]}社가 국내에서 서비스하는 "{gameName[userNumber]}" 에 대해 22.9月 경 등급이 조정되었습니다.',
"해당 게임은 현재 플레이스토어, 앱스토어, 원스토어에서는 15세 이상 이용가능 으로 등급분류 되어 있으나 귀 위원회의 권고 처분으로 인해 등급이 상향되었습니다.",
"대상 게임은 모든 유통사에서 15세 등급물로 분류되어 있으나 귀 위원회의 재심사 처분으로 청소년 이용 불가 게임으로 조정을 받았습니다.",
"해당 문화컨텐츠는 각 유통사에서 15세 미만 이용불가로 등록되어 있으나 게임물관리위원회의 재심사 및 등급상향(청소년 이용불가) 조정 처분을 받았습니다.",
f"모바일게임 ({gameName[userNumber]})는 구글 플레이스토어 등에서 15세 등급물로 분류되어 서비스되고 있습니다.그러나 근래에 담당 부서로부터 청소년 이용불가 판정을 받았다고 합니다.",
f"안드로이드 폰게임 {gameName[userNumber]}는 이미 15세 이상 이용가능 등급분류를 받고 서비스되고 있으나 게임물등급관리위원회의 재심사에 의해 청소년 이용 불가 판정을 받았다는 것을 확인했습니다.",
'현 게임물관리위원회는 여러 게임물에 대해 기존의 이용등급 결정을 번복하고 새로운 이용등급을 지정하였습니다.',
'게임물관리위원회의 이번 결정은 본 민원인이 보기에 권력 남용이라고 봅니다.서비스중인 게임에 대한 심의등급 재심사는 신중하고 합리적으로 진행되어야 하는 것이지, 이렇게 번개불에 콩 볶아 먹듯 진행되야 하는게 아닙니다.',
'게임물관리위원회는 왜 서비스 초기나 게임물 업데이트 당시에 심의등급 상향 조치를 취하지 않고 7개라는 소수의 민원글만 보고 몇 달 동안 모니터링한 사항이라고 하면서 심의등급 조정을 진행하려고 하는지 이해가 가지 않습니다.',
)
fire1_1 = (
f"하지만 해당 게임 ({gameName[userNumber]}) 은 게임물관리위원회 등급분류규정 개정안 8조 선전성 기준 4-가 에 해당되는성기 등이 완전노출된 것은 아니지만, 선정적인 신체노출이 표현되어 있는 경우해당 경우에 해당하지 않으며 게임 내에서 고등학생으로 소개된 학생들을 대상으로 부적절한 모습 및 왜곡된 성관념을 심어줄 수 있는 장면도 포함하고 있지 않습니다.",
f"해당 게임 <{gameName[userNumber]}> 은 성행위 및 유사성행위를 이유로 등급상향 처분을 받았으나,'게임물관리위원회 등급분류규정'에 의거한 등급분류규정 8조 4번 선정성으로 인한 청소년 이용불가 등급에 부합되지 아니하며하나의 문화예술중 하나인 {gameName[userNumber]}와 와이푸를 비롯한 다른 일반적인 청소년 이용불가급 음란물 게임과는 비교조차 될 수 없다고 생각합니다.",
f"해당 게임[{gameName[userNumber]}]에서는 '게임물관리위원회 등급분류규정'에 의거, 등급분류규정 8조 4번 선정성으로 인한 청소년 이용불가 등급에 부합되지 않습니다.",
f"또한 '{gameName[userNumber]}' 이러한 게임은 게임관리위원회 등급분류규정 청소년 이용 불가등급 기준 가 항의 경우 선정성에 관한 법원 판례 대법원 2013. 11. 14., 선고, 2011두11266 에 따르면'선정성 측면에서 청소년 이용불가의 등급분류기준을 충족하는지 여부는 해당 영화를 전체적으로 관찰하여 신체 노출 및 성적 행위의 표현 정도뿐만 아니라그 영상의 구성 및 음향의 전달방식, 영화주제와의 관련성, 영화 전체에서 성적 표현이 차지하는 비중 및 그 영화의 예술적·교육적가치 등을 종합적으로 고려하되, 제작자의 주관적인 의도가 아니라 사회의 일반적인 통념에 따라 객관적이고 규범적으로 평가한다' 라고 되어 있습니다."
)
fire1_2 = (
"게임상 내용과 포함된 이미지에서 직접적인 나체 표현, 도촬, 유사성행위 혹은 성행위 등의 선정적 연출과 이에 대한 직접적 묘사가 없고간접적이고 제한적으로(사람의 형상을 띈 존재들이 성적인 부위를 신체적 접촉을 하지 않음) 표현하고 있습니다.이것은 게임물관리위원회 등급분류규정 8조 4번 청소년 이용불가에 해당되지 않는 내용입니다.",
"직접적인 성행위, 유사성행위 및 이를 종용하는 내용이 포함되어있지 않습니다. 이는 명백히 게임물관리위원회 등급분류규정 8조 3번 15세 이용가에 해당되는 내용입니다.",
"성 윤리에 위배되는 컨텐츠라 보기 어렵습니다. 그러므로 게임물관리위원회 등급분류규정 8조 3번 15세 이용가에 해당되는 내용이라고 생각합니다.",
"통념적인 성 관념을 위배한다고 볼 수 있는 내용은 존재하지 않는다고 생각합니다. 그렇기에 게임물관리위원회 등급분류규정 8조 4번 청소년 이용불가에 적용되기에는 다소 무리가 있습니다.",
"선정적인 행위를 하도록 유도하거나 구체적이고 직접적으로 조작할 수 있는 일반적인 사회윤리에 어긋나는 컨텐츠에 비견되기는 어렵기에 게임물관리위원회 등급분류규정 8조 4번 청소년 이용불가라는 규제는 이해하기 힘듭니다."
)


Notice34=(
    "1. 위원회는 이용등급을 결정한 게임물에 대해 별지 제10호의 등급분류증명서를 신고인에게 교부하여야 한다.",
    '2. 위원회는 등급분류 결정 통보 시 해당 신청자에게 결정근거와 결정사유 및 게임물 내용정보가 명시된 별지 제11호의 등급분류결정서를 교부하여야한다.',
    '① 위원회는 이용등급을 결정한 게임물에 대해 별지 제10호의 등급분류증명서를 신고인에게 교부하여야 한다. <개정 2022.9.22.>',
    '② 위원회는 등급분류 결정 통보 시 해당 신청자에게 결정근거와 결정사유 및 게임물 내용정보가 명시된 별지 제11호의 등급분류결정서를 교부하여야 한다. <개정 2022.9.22.>',
    '1. 위원회는 이용등급을 결정한 게임물에 대해 별지 제10호의 등급분류증명서를 신고인에게 교부하여야 한다.2. 위원회는 등급분류 결정 통보 시 해당 신청자에게 결정근거와 결정사유 및 게임물 내용정보가 명시된 별지 제11호의 등급분류결정서를 교부하여야한다.',
    '① 위원회는 이용등급을 결정한 게임물에 대해 별지 제10호의 등급분류증명서를 신고인에게 교부하여야 한다. <개정 2022.9.22.>② 위원회는 등급분류 결정 통보 시 해당 신청자에게 결정근거와 결정사유 및 게임물 내용정보가 명시된 별지 제11호의 등급분류결정서를 교부하여야 한다. <개정 2022.9.22.>',
    '① 위원회는 이용등급을 결정한 게임물에 대해 별지 제10호의 등급분류증명서를 신고인에게 교부하여야 한다.',
    '② 위원회는 등급분류 결정 통보 시 해당 신청자에게 결정근거와 결정사유 및 게임물 내용정보가 명시된 별지 제11호의 등급분류결정서를 교부하여야 한다.',
    '① 위원회는 이용등급을 결정한 게임물에 대해 별지 제10호의 등급분류증명서를 신고인에게 교부하여야 한다.② 위원회는 등급분류 결정 통보 시 해당 신청자에게 결정근거와 결정사유 및 게임물 내용정보가 명시된 별지 제11호의 등급분류결정서를 교부하여야 한다.'
    )

Notice1=(
    f'그리고 게임물 관리 위원회 등급분류 규정에 따르면 제 34조 등급분류 결정통보에"{randomLine(Notice34)}"라고 쓰여있습니다.',
    f"또 다른 건으로는 지난 2022년 9월 22일에 개정된 게임물관리위원회의 등급분류 규정인 제34조 등급분류 결정통보에는'{randomLine(Notice34)}'이렇게 쓰여있는것을 확인했습니다.",
    f'그리고 게임물관리위원제 등급분류규정 제34조 등급분류 결정 통보에 따르면"{randomLine(Notice34)}"라고 규정되어 있습니다.',
    f"이러한 민원을 적는 이유중 하나인 게임물 관리 위원회 등급분류 규정에 제 34조 등급분류 결정통보에는'{randomLine(Notice34)}'라고 적혀있는것을 확인했습니다.",
    f'게다가 2022년 9월 22일 개정된 게임물관리위원회 등급분류 규정에 따르면 제 34조 등급분류 결정통보"{randomLine(Notice34)}"이렇게 쓰여있습니다.',
    f'또한 게임물관리위원회의 등급분류에 따르면 제 34조 등급분류 결정통보"{randomLine(Notice34)}"라고 규정되어 있습니다.'
)

Notice2=(
    '하지만 이 기사를 참고해보면 소녀전선측의 공지사항에 보면 이메일과 유선전화등 할 수 있는 모든 방법으로 연락을 하였으나 연락받지 못했다는 글이 게시되었습니다.http://www.enewstoday.co.kr/news/articleView.html?idxno=1606397 이러한 일이 일어난 이유가 무엇이고 앞으로 이런 일이 일어나지 않도록 어떻게 해결 할 것인지에 대한 답변을 부탁드립니다.',
    '그렇지만 해당 기사를 보면 소녀전선측 게임사는 공고조차 받지 못했다는 것을 알 수 있었습니다.http://www.newscape.co.kr/news/articleView.html?idxno=89601 해당 사태가 일어나게 된 이유와 앞으로 유사한 사태가 일어나지 않도록 솔루션 제공을 요구합니다.',
    '그러나 아래의 게시글을 보다시피,소녀전선의 담당자가 모든 할 수 있는 연락책으로 연락을 해보았지만 연락이 닿지 못했고 관련 내용의 파악 및 대처를 전혀 하지 못하였음을 보여줍니다.https://www.inven.co.kr/webzine/news/?news=277535&site=girlsfrontline 이런 결과가 나온 이유가 무엇인지 앞으로 어떻게 해결해 나갈것인지에 대한 답변을 요청합니다.',
    '허나 소녀전선이라는 게임의 공식카페에 이러한 글이 올라왔습니다.https://cafe.naver.com/girlsfrontlinekr/4472675 게임관리위원회에게 등급재분류 상황에 대해 아무런 연락도 받지 못하였고 이메일,유선전화등 모든 연락수단을 이용해 연락을 해보았으나 게임관리위원회에게 연락이 닿지 못했다는 공지입니다.어떤 행정처리가 잘못되어 이러한 결과가 나왔는지,이에대한 해결책은 무엇인지 알려주시길 바랍니다.',
    "하지만 여기 게제된 기사를 보면 '명일방주'와 '소녀전선' 게임 관리자 측은 게관위에게 전혀 통지 받은 바가 없다고 합니다.http://www.newscape.co.kr/news/articleView.html?idxno=89601 해당 사건에 대한 충분한 설명 및 해결책을 제시해 주시길 요청합니다."
)

infoOpenLaw = (
    '제15조(회의록의 작성 등)① 위원회의 모든 회의는 회의록을 상세히 작성하고 위원이 기명날인 또는 서명하여야 한다. 필요한 경우에는 회의를 녹취 또는 녹음할 수 있다.② 회의록은 차기 회의에서 보고하며, 위원회 위원이 이의를 제기한 때에는 그 사유를 기재하여야 한다.③ 위원회는 회의록 등 각종 기록을 전산처리하여 투명성, 공정성을 제고하여야 한다.',
    '제15조(회의록의 작성 등)① 위원회의 모든 회의는 회의록을 상세히 작성하고 위원이 기명날인 또는 서명하여야 한다. 필요한 경우에는 회의를 녹취 또는 녹음할 수 있다.② 회의록은 차기 회의에서 보고하며, 위원회 위원이 이의를 제기한 때에는 그 사유를 기재하여야 한다.③ 위원회는 회의록 등 각종 기록을 전산처리하여 투명성, 공정성을 제고하여야 한다.제16조(회의록의 공개) ① 위원회의 회의록은 공개한다. 다만, 다음 각 호의 1에 해당하는 경우에는 위원회의 의결로써 공개하지 아니할 수 있다.1. 다른 법률 또는 법률이 위임한 명령에 의하여 비밀로 분류되거나 공개가 제한된 사항2. 법인, 단체 또는 개인의 명예 및 영업비밀의 보호 등 공개될 경우 정당한 이익을 해칠 특별한 사정이 인정되는 사항3. 감사·감독·검사·규제·입찰계약·인사관리·의사결정과정 또는 내부검토과정에 있는 사항 등으로서 공개될 경우 공정한 업무수행에 현저한 지장을 초래한다고 인정할 만한 사유가 있는 사항② 회의록의 열람 및 복사를 원하는 자는 열람 및 복사의 목적을 포함한 별지 제3호 서식의 신청서를 작성하여 제출하여야 한다.③ 위원회는 접수일로부터 10일 이내에 회의록의 공개여부를 결정하여 지체 없이 신청인에게 서면으로 통보하여야 한다.④ 기타 회의록 공개 및 정보공개와 관련하여 필요한 사항은 위원회 세칙으로 정한다.',
)

infoOpen1 = (
    f'또한 아래의 게임물관리위원회의 회의록 규정 제 15조(회의록의 작성등)에 따라 정보공개를 요청합니다.{randomLine(infoOpenLaw)}'
    f'그리고 {randomLine(infoOpenLaw)}위에 있는 규정에 의거하여 정보공개를 청구합니다.',
    f'{randomLine(infoOpenLaw)}위에 있는 게임물 관리규정위원회 제15조 1항 및 3항에 따라 본 민원인은 정보공개를 요청합니다.',
    f'{randomLine(infoOpenLaw)}이와같이 규정된 게임물관리규정위원회의 15조 규정 1항과 3항에따라 민원인은 정보공개를 청구합니다.',
    f'다음으로 하단의 게임물 관리규정위원회의 규정 15조 1항,3항을 이유로 정보공개를 요청합니다.{randomLine(infoOpenLaw)}'
)

infoOpen2=(
    f'또한 {gameName[userNumber]} 이외에도 {gameName[userNumber-1]},{gameName[userNumber-2]}와 같은 게임들도 등급상향이 되었습니다. 이에 관한 회의록 전체를 공개하여 공지하는것을 강력하게 요청합니다.',
    f'더불어 {gameName[userNumber]}와 함께 {gameName[userNumber-1]}나 {gameName[userNumber-2]}의 게임도 선정성을 이유로 등급 변경이 이루어졌습니다. 이에 관련된 회의록의 전체 공개 및 공지를 강력요청합니다.',
    f'심지어 {gameName[userNumber-1]}과 {gameName[userNumber-2]}와 같은 게임도 같이 등급상향이 되었는데 이것들의 심의 회의록도 같이 공개하는것을 강력하게 요구합니다.',
    f'{gameName[userNumber]} 외 선정성을 이유로 등급상향이 된 다른게임들과 관련된 2022년 1월 1일 ~ 오늘 까지의 회의록을 공개할것을 강력하게 요구하는 바이며, 앞으로 더욱 신의에 부합하는 행정업무를 소망합니다.',
    '솔직히 해당 행정처리는 불상사라 생각하고 적지않은 불쾌감을 느끼고 있습니다.더불어 이와 관련되어 있는 2022년1월 1일 부터 작일까지의 모든 회의록의 공개와 공지를 강력히 요구하는 바입니다.',
    '본 민원인은 게임물 관리 위원회의 2022년 1월 1일 ~ 금일까지의 회의록을 모두 공개하여주시기를 요청합니다.',
    f'본 민원인은 등급분류 회의록의 사본 또는 열람(기간은 {infoYear}년 1월 1일 ~ {infoYear}년 12월 31일 까지) 을 강력히 요청합니다.',
    f'민원인은 등급분류 회의록의 사본 또는 열람({infoYear}년 1월 1일 ~ {infoYear}년 12월 31일 까지) 정보공개를 청구합니다.',
    '또한 선정성으로 인한 등급 변경을 굳이 게이머에게 제대로 고지도 안한 채 빠르게 변경이 된 이유가 현재 항간에 떠도는 소문같이 보복성으로 이루어진것이 맞는지 궁금합니다.',
    f'{gameName[userNumber]}의 행정처리와 관련된 2022년 회의록들에 대한 정보공개를 강력하게 요구합니다.',
    f'게임관리위원회의 {infoYear}년 1월 1일 ~ {infoYear}년 12월 31일 까지 의 해당 회의록들 전체를 공개하는것을 요청하는 바입니다.',
    f'현재 기재되어있는 {infoYear}년 1월 1일 부터 {infoYear}년 12월 31일 까지의 등급분류 회의록들을 모두 투명히 공개하도록 하여 공지해주실것을 요청합니다.',
    '게임관리위원회의 2022년도 1월 1일 부터 민원 접수 당일까지의 회의록 공개를 강력하게 청구합니다.',
    '해당 이미 심의되어진 해당 게임이 15세 이용가에서 등급상향이 이루어졌는데 이와 관련된 게임관리위원회의 2022년도의 회의록에 대한 정보공개를 부탁합니다.',
    '게임관리위원회의 2022년도 1월 1일 ~ 현재까지의 회의록 정보공개를 강력하게 요청합니다.',
    '게임관리위원회의 2022년 1월 1일 부터 금일 까지의 관련 기록 문건에 대해 귀 위원회의 불편함을 이해하는 와중에도 정중히 정보공개를 요청합니다.',
    f'게임관리위원회의 회의록의 시본 혹은 열람({infoYear}년 1월 1일 ~ {infoYear}년 12월 31일 까지)을 요청합니다.',
    f'게임관리위원회의 {infoYear}년 1월 1일 ~ {infoYear}년 12월 31일 까지의 회의록의 사본 또는 열람을 요청합니다'
)

infoOpen3 = (
    '만약 회의록을 비공개 또는 부분공개, 정보의 비존재 등으로 처리할 경우 그 이유를 상세히 적어 주시길 바랍니다.',
    '만약 해당 회의록이 공개처리가 되지 못한다면 그 이유를 상세하게 적어 주시면 감사하겠습니다.',
    '행여나 회의록이 공개처리가 되지 않는다면 공개를 못하는 이유가 무엇인지 자세히 적어주시길 바랍니다.' ,
    '혹시라도 희의록의 부분 공개나 정보의 부존재, 비공개등으로 처리될 경우 그 이유는 무엇인지 최대한 자세히 답변해주시면 감사하겠습니다.',
    '회의록이 비공개, 정보의 부존재등으로 처리가 되는 경우, 처리된 이유가 무엇인지 알기 쉽게 풀어서 설명해주기 바랍니다.',
    '회의록을 공개처리하지 못 할 경우, 그러한 이유가 무엇인지 자세한 설명 부탁드립니다.',
    '회의록이 비공개,부분공개,정보의 비존재 등으로 처리되는 이유가 있을경우 그 이유를 자세하게 설명해주길 바랍니다.'
)

ending=(
'귀하의 노력에 감사합니다.',
'이상 해당 민원에 대하여 긍정적인 검토를 해주셨으면 감사하겠습니다.',
'고생하는 시장이하 모든 공무원들에게 경의을 표하는 바입니다',
'민원 신청에 외국인 친구 게시물의 도움을 받았습니다. 적극 검토 부탁드립니다.',
'추신.민원 신청에 민간 법조인의 도움을 받았습니다.',
'저도 민원을 쓰는건 드문 일이라 맥락과 문맥이 다소 맞지 않을 수 있습니다.',
'전문종사자가 아니기에 발췌한 법령 해석에 다소의 오류가 있었다면 감안 부탁드립니다.',
"다소 가독성 및 오탈자에 양해 부탁드립니다.",
'띄어쓰기,가독성,맞춤법 부분에 대해서는 양해 부탁드립니다.',
"본 민원의 공정한 판단을 바라며 이만 글 줄이겠습니다.",
'이에 본 민원인은, 귀 게임물관리위원회의 이번 일련의 게임물 이용등급 재조정 조치를 철회함이 좋겠다고 생각합니다. 신속한 민원처리 부탁드립니다.',
'긴 글 읽어주셔서 감사합니다. 이에 결정 번복과 향후 유사사례 발생 방지를 위한 대책 마련을 공지해주시길 바랍니다.',
'저도 글을 잘 쓰는 편은 아니라 문맥이 이상한 점은 양해 부탁드립니다.',
'민원은 정당한 국민의 권리입니다. 성심성의껏 처리해주시길 부탁합니다.',
'민원 처리의 공명정대한 일처리를 부탁드리겠습니다.',
'그러므로 본 민원인은 귀 위원회의 이번 일련의 조치에 대한 철회를 요청합니다. 신속한 일처리를 부탁드립니다.',
'본 민원인은 이번 게임물관리위원회의 결정에 큰 유감을 표하고 귀 위원회의 결정을 번복하였으면 합니다. 감사합니다.',
'앞으로 이런 일이 반복되면 국내 게임산업의 성장은 크게 정체되고, 개발자들이 누리던 표현의 자유는 크게 침해될 것이라고 봅니다.따라서 개발자들의 표현의 자유를 존중하기 위해서라도, 이번 결정은 취소해야 할 것입니다.',
'게임물관리위원회의 행보에 의문이 느껴지는 점이 많습니다. 부디 상식과 공정이 살아있는 업무처리 부탁드리겠습니다.',
'본 민원인은 최근 귀 위원회의 업무처리에 느끼는 실망감이 큽니다. 저를 포함해 모두가 납득할 수 있는 답변을 기다리겠습니다.',
'게이머의 편이라던 게임물관리위원회의 포부는 아직 건재하다면 함께 게이머의 편이 되어주시길 바라며 공정한 민원처리를 요청합니다.',
'현재 게임물관리위원회의 전문성에 대해 의문과 우려를 표하는 목소리가 큽니다. 전문성 있는 답변을 기다리며 민원 마치겠습니다.',
'아울러, 최근 민원 거부에 관한 논란에 대해서도 귀 위원회의 현명한 대처를 기대하며 이만 민원을 마칩니다.',
'귀 위원회가 민원을 거부한다는 타 민원인의 의견이 나오고 있습니다. 부디 이번 민원은 성실히 처리해주셨으면 합니다.',
'또한, 앞으로 민원을 거부한다는 이야기가 나오지 않게, 진정성 있는 민원 처리를 부탁합니다.',
'기업들이 행정부의 일관된 처분을 기대할 수 있도록 하여, 게임산업의 지속적인 발전에 기여하여 주시기 바랍니다.',
'국민들이 행정부의 일관된 행정을 기대할 수 있도록 하여, 문화여가 권리의 보장에 기여해주시길 촉구합니다.',
'오인에 의한 해당 위원회의 잘못된 판단을 시정할 수 있도록 해주시길 거듭 당부드립니다.',
'해당 위원회의 오판을 지적해주시어 재검토 및 시정될 수 있도록 신경써주시길 부탁드립니다.',
'당 부처가 국민으로부터 받는 신임만큼 강단있고 신실한 행정시정을 당부합니다.',
'불의에 대한 행정부처의 올바른 자세을 기대할 수 있도록 하여, 국민의 신뢰와 신의에 적극 보답해주시길 바랍니다.',
'다소 이의가 있을지라도, 귀 위원회의 판단에 대해 이후 과도한 선례가 만들어지지 않도록 하여, 국민을 짓누르는 거대한 국가가 되는것을 지양해주시길 바랍니다.',
'국민의 권익보호에 힘써주시어 항상 감사합니다.',
'국민의 정당한 권리가 행정부의 졸속 행정으로 침해받는 사안에 대해 신실한 업무를 당부드립니다.',
'담당 공무원 혹은 위원장님께선 게관위가 국민의 권리를 침탈하는 정무처라는 오명을 탈피 해주시길 진심으로 바랍니다.',
'비전문가만 임용된 졸속정무처라는 과거로부터의 프레임에서 벗어나 아이들을 위한 건전한 행정업무에 더욱 힘써주시길 염원합니다.',
'국민의 목소리에 귀 기울여 앞으로 비전문적 규제위원회라는 오명을 벗으실 수 있기를 소망합니다.',
'국민과 청소년을 위한 건전한 등급분류에 떳떳한 행정처의 판단을 바랍니다.'
)
macro1_1 = (
'공무원에게 봉사(공익, 국민, 국익, 청렴, 투명행정...)는 무슨 의미를 갖는다고 생각하십니까?',
'공직가치 중에서 제일 중요하다고 생각하시는 것은 무엇이라고 생각합니까?',
'공무원 헌장 전문이 무엇입니까?',
'공무원의 신조가 무엇입니까?',
'헌법 7조1항, 2항이 무엇입니까?',
'국민이 생각하는, 똑바른 공무원 상이 무엇이라고 생각합니까?',
'공무원의 6대 의무가 무엇입니까?',
'귀 부처에서 가장 중요한 공직가치가 무엇이라고 생각합니까?',
'태극기의 사괘의 의미가 무엇인지 아십니까?',
'해당 민원 답변자의 직위는 어떻게 되십니까?',
'위 민원에 대해 발언자의 의견은 어떻게 되는지 궁금합니다.',
'현재 대한민국의 국화이자 애국가의 후렴구에 나오는 꽃의 이름은 무엇입니까?',
'이러한 사태의 재발 방지 대책은 어떻게 되는지, 그리고 이번사태를 어떻게 처리할 것인지 다시한번 문의드립니다.',
'선정성으로 인해 등급이 상향되었는데 선정성에 대한 내부의 주관적이고 확실한 기준이 무엇이며 어떠한 명목으로 처리되었는지 궁금합니다. 꼭 답변 부탁드립니다.',
'대한민국 동쪽 바다의 이름은 무엇인지 답변 해주세요.',
'독도 및 울릉도가 속해 있는 바다의 이름을 적어주시면 감사하겠습니다.',
'서브컬쳐 유저들의 민원을 악성민원으로 취급하고 있습니까? 아니라면 왜 민원들의 대한 답변이 모두 동일한지, 답변이 늦는 이유가 무엇인지 알려주시길 바랍니다.'

)

fire1 = (randomLine(fire1_1),f'게임물관리위원회 등급분류규정 제 8조(선정성 기준)3. 15세이용가: 선정적 내용이 있지만, 간접적이고 제한된 경우4. 청소년이용불가: 선정적 내용이 표현되어 있으나 사회질서를 문란하게 할 정도는 아닌 경우라고 쓰여있고 해당 게임은 가슴과 둔부가 묘사되나 이에 대한 표현은 선정적이지 않으며,{randomLine(fire1_2)}')
macro = (f'끝으로 매크로 답변이 오는것을 방지하기 위해 한가지의 질문에 답변해주시기 바랍니다.{randomLine(macro1_1)}만약 이 질문에 대한 답변이 어려운경우 구체적인 사유를 적어 왜 답변하기 어려운지 알려주시면 감사하겠습니다.',
f'이상으로 본문을 제대로 안 읽고 건성으로 답변 하는것을 방지하기 위하여 간단한 질문의 답을 해주시면 감사하겠습니다.{randomLine(macro1_1)}위의 대한 답변이 불가능 할 경우 왜 안되는 것인지에 대한 사유를 구체적으로 적어주시면 감사하겠습니다.')
fixLaw= (f"""그리고 게임물관리위원회는 등급분류 규정 40조에 따라 이해관계인의 의견을 청취하고 이를 위원회 규정에 반영하여야 한다고 알고 있습니다.현재 "{gameName[userNumber]}"의 등급 상향으로 인해 게임 이용에 영향을 받는 이해관계인으로서 규정 33조 (이의신청의 절차 등)의 수정을 요구합니다.제 33조 (이의신청의 절차 등)의 '게임법 제23조 제1항에 따른 등급분류의결정 또는 거부결정에 대하여 이의가 있는 자 '에 게임물 이용자 또한 포함 될 수 있도록 내부규정의 수정을 강력히 요구합니다.현재 게임물 관리위원회의 등급관리 방식은 오직 위원회와 게임사의 입장만을 대변할 뿐입니다.이용자의 권리는 철저히 무시당하고 있으며 이에 대한 대책이 시급한 상황입니다.대한민국 게임물의 발전과 이용자의 권익 증진을 위하여 이용자 또한 등급분류의 결정에 이의를 제기할 수 있도록 개정을 요구합니다.""",
f"""같은 맥락의 요구사항이 하나 더 있습니다.게임물관리위원회 등급분류규정 제 40조(의견수렴)'위원회는 게임법 시행규칙 제8조 제4항에 따라 등급분류기준 및 사행성 확인기준에 관한 위원회 규정의 적실성을 확보하기 위하여 매년 1회이상 이해관계인의 의견을 청취하여야 하며 이를 위원회 규정에 반영할 수 있다' 라고 규정되어 있습니다."{gameName[userNumber]}"의 등급 상향으로 정상적인 게임 이용에 영향을 받는 게이머인 이해관계인으로 규정 33조'이의신청의 절차'의 수정을 요구하는 바입니다.제 33조 (이의신청의 절차등)의 '게임법 제 23조 제1항에 따른 등급분류의결정 또는 거부결정에 대하여 이의가 있는 자'의 범위를 게임물 이용자도 포함될 수 있도록 내부규정의 수정을 강력하게 요구합니다."""
)
words = (greeting, now, fire1,Notice1, Notice2, infoOpen1, infoOpen2, infoOpen3, fixLaw, macro, ending)
def randHead(Name):
    gameName = Name
    return randomLine(title)
    
def randBody(Name):
    gameName = Name
    word = ''
    for i in words:
        word += f'{randomLine(i)}\n'
    return word



app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET','POST'])
def start():
    return '태초마을이야!'
@app.route('/order/', methods = ['GET'])
def index():
    gameName = request.args.get('gameName')
    return ({'title':f'{randHead(gameName)}', 
            'body':f'{randBody(gameName)}'
            })



# app.run(port=5002, debug=True, host=0.0.0.0) 
if __name__ == "__main__":
    app.run(port=5002, debug=True)

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
