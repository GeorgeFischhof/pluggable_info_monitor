
import datetime

from PIM_constants import DisplayParts, InfoSeverity


def get_info():
    left = {
        'display_part': DisplayParts.HALF_LEFT,
        'info_severity': InfoSeverity.INFO,
        'info': 'Some info for left hand side ;-)',
    }

    right = {
        'display_part': DisplayParts.HALF_RIGHT,
        'info_severity': InfoSeverity.INFO,
        'info': """
            Here comes an inline image. It is base64 encoded.
            If you save a webpage with inline image, it is saved 
            into one html file.
            <br><br>
            <img src="data:image/png;base64,
            iVBORw0KGgoAAAANSUhEUgAAAO0AAABu
            CAMAAAD8t2TLAAAAGXRFWHRTb2Z0d2Fy
            ZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAA
            AC1QTFRF////LVcpkauOZYdhrsStx9jF
            1uTV+//66PPn8vzy4uji7vft4O3f+P/3
            8fPwC7dd6gAACdxJREFUeNrsXIti2yoM
            NYiHiSH//7kXCXD8AmTaddudta1zEht0
            QOhIgnSaHnnkkUceeeSRv1vszzRlv7Oj
            L2hoUZEwTSHUNHIsoLYJ1oYBvE2tjnfu
            1Nw85DbNWCVAxysvgS7OgxEcR8vglfIN
            tDJ1cxNuRaur7t1OTUfoSPtNM1GLKHqa
            BUk4aakBP+73plBC9XONrbP03opJWs3d
            G1FLoT6vVeqMtFeTBZFQkhYCbEILFS37
            es2Etq6W4up99dTSXUewmyvrduj8RFMa
            YauMNtD/8ro/sN+FdhlB2x3sEBJas5uj
            FZ2c/O61CGl0TKW/8E1oYfolaO0idpOV
            p3qdy5AuVrRzuqGy3hgG6H4J2jJHXWcm
            xNYGk6FGS07rXtrkp4plRzj6utklW353
            eA3DSzH0PnsflitXeyertiBV5FfioNye
            JDTB1dSUthc4xL+z0q6n90A8gEzCoVxZ
            YJSXH5BIsvgZtRN6w6tyBFJFq2kAeyFC
            mIbEah7lhn2AswEp87wrIQ0n2lLN/nSx
            m6+GCNf+j70GYoBjdvFMcryFZMlxM+Dm
            CKRNdr4TIuhBtIHr35boOPTRUxxpSH/V
            M2a0S8eDqEG0qXnorwONftKeu1V5jhUP
            rWpqa3uD/0W0+fl+PHWIXfPcFkvOEQUX
            be2+atD5PWhLKD/z0No9C5CbTsFyqMRP
            l5Zcd7oOoAnmS+vW2uwk+4Pi9JED14km
            cjWy75MDeSk511gP/X5YTIsSk08eqRuE
            KRBx2v6gBNtMsB2PA4MP1NQsL1nEOmcW
            ojq8pxcjzHcn1kCb3A7pc8u+OByI3Uky
            pmuWoUULsERzx/lvxgjNG+rUxwlcdWet
            KF60n5MHX0lPs4sSnhRrBFTZr99Dmxtn
            5Imq4wfVjWZKsn+R+eV0wyX/3uPkm64q
            N86ILDhouc1AnVML9yf/Dp10+yYN5TH6
            YbSFmutoc22klvaXdPsu6ep2RPBx1r11
            q3l9q22yr2oKSZsXtmun2wMhhsFaol3Z
            LhwSzfmjRtN1AystIQpAlwuXaS727xfl
            yaEAkrutZVGCF8pcPJ2qpZQ4+pDpbKKC
            IsxEoimhJKJshR8Bb2mXpIN3HhuxmXft
            oQUfiko4B1ExexUPJb6WfgAsWiGFUhik
            CMC4dy2eUrKwKRarVnElKqDmdkmawMRR
            oQDiSOHUY+zQKDI3lw3ggjblPJ7Ny7QE
            lm1Oowo7ldqTSJW2eh/pcTAdKzaTkwAg
            3dkV6I0/1kUdfTfO5mV8mRYyWrCLONSI
            XXOlWAcdCiyZngGUnCDC8YbsoTbq3Muh
            mLXisCubFspb0eZ6oqy3M4bWnlhOHdS5
            lx93fVQJ49QW3nLY7XDFBDpR6E2026Wh
            PkHjVp3vRZssB5+GTXbuM/V90lfRqfPr
            DinoHdr5XEnXG5tC71Sphahh8ilUnVyf
            hTU7TxZrwiZ9LXlllYCa+W0hSU1eCncr
            02u/K+KWooBave91ukWlzoFVixjpWTfb
            izT9k76W+ngr/218PqWkViZXkfPTFU0u
            3tKo2oCDHDTqYyuuhtoYSOd92mQO3pi5
            nb42ybyX/8aJRJK0h/zUfopvngwpZvPE
            xbPWmt4IZrmg3LRFcRdu5ECgcM2g9PJJ
            M5z/Zk63hxr2B2zun7gdfJxZkmgRl3rN
            QvCKEGcU0ZgSWBMGq6L9HEnv0/dC5vMe
            bVj7WdEu+P5SyYH0ANroZp1hze042sOm
            WSHn8DHNK7TGpve9veZ2NYJWp6H1YfrF
            aOEYv21s8wqtn+wL33/Z67z8LtoUmtIQ
            No+6aMHIb7to1SGP3bS3JNsq/VhCG7KF
            n41Oj3GuTAbVzOVKpVxnrqg11MoIyKfv
            EjzvtulrHG/yvaWf4LWnmu5ifDinwXZw
            /1Zxn6K+G4OSU+N6OJ62eg95NeW6lpq3
            h/3fsq98PClGifRoxke9KI5RONz20vVe
            whL/NCJUediF1olE4hgutuzr68POi07k
            q9w+DR7fvy1JdHdyVfvoR4x/BdSt+cSR
            NoWIQUkUd/IN5XXAQTbfFScrZgF9bqPN
            uUstJTxzJKGFKRBYaU6erLym8zWfuRz0
            x3efbqMt+XDVSI4cmdL1yAf30IbwFbTl
            acm15NCuXYBjjmreMAhWcdCu3X5qKkNT
            m5/uLVybzpXWj/UsGe3C5WxfsnZCu5w4
            dF23CNYfd3MG122pu7sOWKIQ20hfZwWN
            omM+xSuPXO+nJcLFx+yxaLpyr9mN8VoC
            HYKLWna3mctpoanDp43893xDPkkUMtee
            KbSc5bLX79+nXOsSW3OqsM0yTD//Pd9g
            14J5bSuiwq2DnBt9hzT9MfI916A4+e/F
            hq0uBfvr1mvxuRmrslrgnB7qO0LW/u55
            g3d/8texc6+xM6y5Rt11512SY6GFKppa
            RbyD9u7CZR77sz+C9lysbqO9e/Z8PTTO
            Cy/NaF2qtjD1rkJ/LlY31y2o2zTEPNJV
            Duzaxue6VcatfJ45tey8VfPqcM5vY0AS
            ffqyBj+sr0QBsxTdK+K2Nm59Y2M38Wmq
            wNY+D7sqEm3gYk3ayRi5pf3lgCeIE6d3
            C+i8L0BRLDQQwShoVkPz6evQzkiXDdj8
            DSuVMlUM4kAaekOq7nerIgrgnCIY5DjH
            2Q2Tlk3Vu29Y0akGEj/5vMHUR8E+IXI/
            9+CdR+7tDR7PzsoUA4CzMqHVGbZmoGBM
            7iDaDnkFHpXDiWvpqDvgnuB9tIxvJA2i
            De0wjBmmndHSdjbImFffQquZRD34HZze
            yYFZcCxZHf2HWJDU8BgH7Ndtj025h3HU
            6HkH2azitveF8/HYo49HtzVryt2W6JJB
            LfRBdM7daQt8teU0IuFrn4cLPczVDa0K
            70hdZ/ozJEyPPPLII4888sgjjzzyyCOP
            PMKUfCBD8O5WeN9LpMJCvJbvCX+xAKbe
            p2Qc/ki8qFZSdlO1MNc7iQVtAQP4gJQb
            tOuv6Yk3XPzKntHCyC9Ay5/bjPaFeOjH
            Xza3IOCthTblmJGQ6+ULq5zidYEWvyoR
            p1aYD1qAV1wX8cl4Q/wUrzWdoEttxS7o
            Wyo0x/T9EZEOi8bXKv5UP4NWRSWjKlK8
            UvkSFcqXEel7RVsqsIQWpIR3vE3u0cI7
            vixo4893fOCdgBDaV8Qau3vH1RKHFH/z
            Df7TsQuTuvkBSya0cb2+1rlNlzSV6nJu
            hXqLeIF/t2hxY/qV0b5wJD9HChAtUGtC
            KvGmniEPHPMA2zeipZlMaMtlHS3OBBC2
            HtrNb19roP1JL5UsGbLJCble7ix5ixaf
            QpWNME200QCmdyqOb9FuLVli7/gVsR+1
            5FfZjcGVlS+rXoomReZFnu++QnvwUgXt
            b/FSf4b8bh7+MXmRy9b/CFpctP/M1GKc
            KvX0yCOPPPLI/0P+E2AAA7JN+/OU8bgA
            AAAASUVORK5CYII=" 
            alt="html_inline_image.png" 
            title="html_inline_image.png">
        """,
    }

    info = [left, right,]
    return info
