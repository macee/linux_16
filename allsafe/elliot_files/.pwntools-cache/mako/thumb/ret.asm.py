# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.766366
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/ret.asm'
_template_uri = 'thumb/ret.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'A single-byte RET instruction.\n\nArgs:\n    return_value: Value to return\n'
def render_body(context,return_value=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,return_value=return_value)
        __M_writer = context.writer()
        from pwnlib.shellcraft import thumb 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['thumb'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if return_value != None:
            __M_writer(u'    ')
            __M_writer(unicode(thumb.mov('r0', return_value)))
            __M_writer(u'\n')
        __M_writer(u'\n    bx lr\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 10, "33": 12, "39": 33, "16": 2, "17": 7, "22": 1, "26": 1, "27": 6, "28": 7, "29": 9, "30": 10, "31": 10}, "uri": "thumb/ret.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/ret.asm"}
__M_END_METADATA
"""
