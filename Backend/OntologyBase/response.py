from MainFrame import response

CONCEPT_SEARCHING_REQUIREMENTS = response.server_error("""
        无效的输入。
        目前支持的参数：
        1. 本体element id
        2. 定义集和编码
        3. 表述

        Input error: no search parameter has been given or parameter combination are invalid.
        Support combination:
        1. element id
        2. coding set and code
        3. representation
        """)