""""""
from blue_krill.web.std_error import ErrorCode


class ErrorCodes:

    CANNOT_FIND_TEMPLATE = ErrorCode("无法找到页面模版")
    # define your error codes here

    def dump(self, fh=None):
        """A function to dump ErrorCodes as markdown table."""
        attrs = [attr for attr in dir(self) if attr.isupper()]
        table = {}
        for attr in attrs:
            code = getattr(self, attr)
            if code.code_num == -1:
                continue
            table[code.code_num] = code.message

        print("| 错误码 | 描述 |", file=fh)
        print("| - | - |", file=fh)
        for code_num, message in sorted(table.items()):
            print(f"| {code_num} | {message} |", file=fh)


error_codes = ErrorCodes()
