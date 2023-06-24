아!달콤쌉싸름한해커톤의추억이여!
https://github.com/BittersweetHackaton2023/HackatonHufs2023

# python manage.py runserver 해서 실행해야됩니다

# views.py
search_book : 입력받은 책을 DB에서 찾아 책에 관한 정보를 반환함.

checkmail : 입력받은 메일주소와 같은 메일주소를 가진 모델을 DB에서 불러와 반환함

mymileage : 입력받은 메일주소와 checkmail함수를 통해 DB에서 해당 메일 주소의 모델를 불러와 마일리지를 반환함.

registeremail : 입력받은 메일주소가 DB에 등록되어 있는지 확인하고 등록되지 않은 메일을 DB에 저장하여 등록함

usemileage : 해당 메일주소로 어떤 책에 얼만큼의 마일리지를 사용했는지 모델로 저장해 DB에 저장함

register_auction : 입력받은 책의 정보와 메일을 바탕으로 도서와 도서를 등록한 사람을 DB에 저장함.

get_book_counts : 특정 책이 얼마나 등록되어있는지 계산하여 반환함.

