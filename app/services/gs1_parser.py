from datetime import datetime


class GS1Parser:
    """
    Parser GS1 Application Identifier.

    Hỗ trợ:
    (01) GTIN
    (10) Batch/Lot
    (11) Production Date
    (17) Expiration Date
    (21) Serial Number

    Separator GS1:
    ASCII 29 (FNC1)
    """

    FIXED_LENGTH_AI = {

        "01": 14,   # GTIN

        "11": 6,    # Production date YYMMDD

        "17": 6,    # Expiration date YYMMDD

    }


    VARIABLE_AI = {

        "10",       # Batch/Lot

        "21"        # Serial

    }



    def parse(self, raw: str):

        result = {

            "raw": raw,

            "gtin": "",

            "batch": "",

            "serial": "",

            "production": "",

            "expire": ""

        }



        if not raw:

            return result



        # Chuẩn hóa separator

        data = raw.replace(
            "\x1d",
            "|"
        )


        index = 0



        while index < len(data):


            ai = data[index:index+2]


            if ai in self.FIXED_LENGTH_AI:


                length = self.FIXED_LENGTH_AI[ai]


                start = index + 2


                end = start + length


                value = data[start:end]


                self._assign(
                    result,
                    ai,
                    value
                )


                index = end



            elif ai in self.VARIABLE_AI:


                start = index + 2


                separator = data.find(
                    "|",
                    start
                )


                if separator == -1:


                    value = data[start:]


                    index = len(data)


                else:


                    value = data[
                        start:separator
                    ]


                    index = separator + 1



                self._assign(
                    result,
                    ai,
                    value
                )



            else:

                index += 1



        return result



    def _assign(
        self,
        result,
        ai,
        value
    ):


        if ai == "01":

            result["gtin"] = value



        elif ai == "10":

            result["batch"] = value



        elif ai == "11":

            result["production"] = (
                self._format_date(value)
            )



        elif ai == "17":

            result["expire"] = (
                self._format_date(value)
            )



        elif ai == "21":

            result["serial"] = value




    def _format_date(
        self,
        value
    ):

        """
        GS1 YYMMDD → YYYY-MM-DD
        """

        if len(value) != 6:

            return value



        try:

            dt = datetime.strptime(
                value,
                "%y%m%d"
            )


            return dt.strftime(
                "%Y-%m-%d"
            )


        except Exception:

            return value