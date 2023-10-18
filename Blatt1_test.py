import re
from gradelib import *

r = Runner(save("xv6.out"))

@test(5, "hello, returns")
def test_hello():
    r.run_qemu(shell_script([
        'hello'
    ]))
    r.match("Hello xv6!$", no=["exec .* failed", "$ hello\n$"])

@test(5, "sleep, no arguments")
def test_sleep_no_args():
    r.run_qemu(shell_script([
        'sleep'
    ]))
    r.match(no=["exec .* failed", "$ sleep\n$"])

@test(5, "sleep, returns")
def test_sleep_no_args():
    r.run_qemu(shell_script([
        'sleep',
        'echo OK'
    ]))
    r.match('^OK$', no=["exec .* failed", "$ sleep\n$"])

@test(10, "sleep, makes syscall")
def test_sleep():
    r.run_qemu(shell_script([
        'sleep 10',
        'echo FAIL'
    ]), stop_breakpoint('sys_sleep'))
    r.match('\\$ sleep 10', no=['FAIL'])

run_tests()