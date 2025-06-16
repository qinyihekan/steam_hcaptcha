import threading
print(f"当前活跃线程: {threading.active_count()}")  # 如果等于max_workers，可能线程泄漏
for t in threading.enumerate():
    print(t.name, t.is_alive())
    print('按次调用steam注册过hcaptcha联系QQ865303096')