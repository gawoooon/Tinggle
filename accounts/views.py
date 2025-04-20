from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm


def signup(request):

    # post일때 처리
    if request.method == "POST":
        # 입력 사항을 바탕으로 폼 객체 만듬
        form = SignupForm(request.POST)
        # 유효한지 확인
        if form.is_valid():
            user = form.save()  # db 유저 생성
            login(request, user)   # 로그인 처리 (세션 기반, 로그인 상태로 브라우저에 ID담은 세션 쿠키)
            return redirect('/')    # 홈으로 리다이랙션
    else: # get이면 빈 폼 보여주기
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})