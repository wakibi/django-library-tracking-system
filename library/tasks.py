from datetime import datetime
from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task
def check_overdue_loans():
    try:
        loans = Loan.objects.select_related('book').select_related('member').filter(is_returned=False, due_date__lt= datetime.today())
        for loan in loans:
            member_email = loan.member.user.email
            book_title = loan.book.title
            send_mail(
                subject='Loaned Book Over-due',
                message=f'Hello {loan.member.user.username},\n\nThe return date for the book "{book_title}" you borrowed is over-due.\nPlease return it immediately!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[member_email],
                fail_silently=False,
            )
    except Loan.DoesNotExist:
        pass
        