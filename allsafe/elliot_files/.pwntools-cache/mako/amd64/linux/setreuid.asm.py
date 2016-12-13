# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.623191
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/setreuid.asm'
_template_uri = 'amd64/linux/setreuid.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: [uid (imm/reg) = euid]\n    Sets the real and effective user id.\n'
def render_body(context,uid='euid',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,uid=uid)
        __M_writer = context.writer()
        from pwnlib.shellcraft import amd64 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['amd64'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if uid == 'euid':
            __M_writer(u'    /*  geteuid */\n    ')
            __M_writer(unicode(amd64.linux.syscall('SYS_geteuid')))
            __M_writer(u'\n    ')
            __M_writer(unicode(amd64.mov('rdi', 'rax')))
            __M_writer(u'\n')
        else:
            __M_writer(u'    ')
            __M_writer(unicode(amd64.mov('rdi', uid)))
            __M_writer(u'\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(amd64.linux.syscall('SYS_setreuid', 'rdi', 'rdi')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 10, "33": 11, "34": 11, "35": 12, "36": 13, "37": 13, "38": 13, "39": 15, "40": 16, "41": 16, "47": 41, "16": 3, "17": 2, "22": 1, "26": 1, "27": 2, "28": 6, "29": 8, "30": 9, "31": 10}, "uri": "amd64/linux/setreuid.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/setreuid.asm"}
__M_END_METADATA
"""
