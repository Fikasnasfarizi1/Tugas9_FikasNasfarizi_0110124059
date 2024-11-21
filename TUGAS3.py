print('##nomor 3##')
def status_kelulusan(nilai):
    if nilai >60:
        return 'lulus'
    else:
        return 'tidak lulus'
    
nilai_kamu = 80
status = status_kelulusan(nilai_kamu)
print(f'nilai: {nilai_kamu} status: {status}')

nilai_kamu = 60
status = status_kelulusan(nilai_kamu)
print(f'nilai: {nilai_kamu} status: {status}')




