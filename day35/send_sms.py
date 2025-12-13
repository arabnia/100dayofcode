from sms_ir import SmsIr
sms_ir = SmsIr( "0mKods2aIU0VwRghMUt4kGgillelxZ3fc2stpuFC2wsCsG3S")
sms_ir.send_sms("+989912005828", "sample02")
output = sms_ir.report_today(10, 10)
print(output.url)
print(output.text)
print(sms_ir.report_today(10, 10))