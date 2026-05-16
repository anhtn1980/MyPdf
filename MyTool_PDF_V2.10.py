from tkinterdnd2 import TkinterDnD, DND_FILES  # Import tkinterdnd2 để hỗ trợ kéo thả tệp
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, messagebox, Menu, Canvas
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import os
import platform
import subprocess
import io
import base64



image_base64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAW4AAAC2CAYAAAD5uGd5AAAACXBIWXMAAAsTAAALEwEAmpwYAAAF"
    "0WlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0w"
    "TXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRh"
    "LyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMxNDIgNzkuMTYwOTI0LCAyMDE3LzA3LzEz"
    "LTAxOjA2OjM5ICAgICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3Jn"
    "LzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0i"
    "IiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5zOnhtcE1NPSJo"
    "dHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFk"
    "b2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpkYz0iaHR0cDovL3B1"
    "cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2Jl"
    "LmNvbS9waG90b3Nob3AvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ0Mg"
    "MjAxOCAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDI0LTA5LTE3VDE0OjEzOjQ4KzA3OjAw"
    "IiB4bXA6TWV0YWRhdGFEYXRlPSIyMDI0LTA5LTE3VDE0OjEzOjQ4KzA3OjAwIiB4bXA6TW9kaWZ5"
    "RGF0ZT0iMjAyNC0wOS0xN1QxNDoxMzo0OCswNzowMCIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlp"
    "ZDo5ZWE0MWVjYS05ZTdlLTE3NGEtYjUwMy04NDExM2QxODIxNGEiIHhtcE1NOkRvY3VtZW50SUQ9"
    "ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDpiZTYxNjdlMC1iMTRmLThkNGEtODBiOC0zZWZjNmY5MDU3"
    "YjEiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3ZGFmNzU4NC1iZTBmLWQ4NGMt"
    "YTNlMC1iMjk5M2FlM2NkNzMiIGRjOmZvcm1hdD0iaW1hZ2UvcG5nIiBwaG90b3Nob3A6Q29sb3JN"
    "b2RlPSIzIj4gPHhtcE1NOkhpc3Rvcnk+IDxyZGY6U2VxPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0i"
    "Y3JlYXRlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo3ZGFmNzU4NC1iZTBmLWQ4NGMtYTNl"
    "MC1iMjk5M2FlM2NkNzMiIHN0RXZ0OndoZW49IjIwMjQtMDktMTdUMTQ6MTM6NDgrMDc6MDAiIHN0"
    "RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE4IChXaW5kb3dzKSIvPiA8"
    "cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6OWVh"
    "NDFlY2EtOWU3ZS0xNzRhLWI1MDMtODQxMTNkMTgyMTRhIiBzdEV2dDp3aGVuPSIyMDI0LTA5LTE3"
    "VDE0OjEzOjQ4KzA3OjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0Mg"
    "MjAxOCAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPC9yZGY6U2VxPiA8L3htcE1NOkhp"
    "c3Rvcnk+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNr"
    "ZXQgZW5kPSJyIj8+Ogs7FAAAHBRJREFUeJztnV9sHNd1xg+X23QodyWqEbnhQ5gIbXYpFjYgGgYI"
    "kQnSOiJtA9YGMVMxaSSRcaEaaODaMMQH2o/RPlAQrLxVrFDJLpDKhdqUFGJVthW0NiUYNWKhbiWb"
    "lAPZsgGVXKVcckFpbJPLPnBmM1rNzN6ZOXfmzu73AwJFJnfmarn87jfnnj9N6+vrBAAAID4kol4A"
    "AAAAb0C4AQAgZkC4AQAgZkC4AQAgZkC4AQAgZkC4AQAgZkC4AQAgZkC4AQDAhVwutz3qNVSTjHoB"
    "AACgIqZgT01NXY96LdXAcQMAQBXZbNfg1q1/WFJRtInguAEAoMLIyOi2c+defWx+fv7lqNfiBoQb"
    "AACIqK+/f+eH167dr7poE0G4AQCA0un0fiKiOIg2EWLcAIAGpq+/f2dLy6ZDRPERbSI4bgBAg5JO"
    "p/cvLBSymUzmzdnZD85HvR4vwHEDABqKXC63vaVl06G4ijYRHDcAoIHIZrsG5+bmvkVEtKtv15mL"
    "MzOXo16THyDcAICGwAyNEMVbtIkQKgEA1Dl9/f07m5oShxcWCllN04p79jx+Is6iTQTHDQCoYywu"
    "e1zTtLG9e/eePHXq5K2o1xWUJgwLBgDUG7lcbvtrr70+pOt6KxGRpmnFehFtIjhuAECdYTmAHCei"
    "fHt722yccrRFQIwbAFAXjIyMbmtp2XSo3kWbCI4bAFAH9PX377x08dIQbQg2UR2LNhGEGwAQc6wH"
    "kMZ/yse1sEYUhEoAALHE7DPSaKJNBMcNAIghNi6biCgf98IaUeC4AQCxwdpnhBpUtInguAEAMaEq"
    "za+CpmljAwO7z6g6ZkwGEG4AgPK0tGw6ZBTT3OWy662wRhQINwBAWSxpfkQ2on3nzu0jUawraiDc"
    "AAAlcTiAJGpw0SbC4SQAQDFcDiCJjMKaRhZtIjhuAIBCOB1AGtR1NaQX4LgBAJFj02ekmnwmk3kT"
    "or0BHDcAIFJquGyiBqmG9AKEGwAQGS4HkCYNVVgjCkIlAIDQsY4TI4i2Z+C4AQChIuCyiYjye/Y8"
    "fqKRqiG9AOEGAIRC1TgxR5etaVqx0UrYvQLhBgBIR+AAkgiFNcIgxg0AkIZAmp8JRNsDcNwAACnY"
    "jBNzAqLtEQg3AIAdwQNIIlRD+gKhEgAAGzX6jFSDakifwHEDAFgQPIA0QTVkAOC4AQCB8HAASUQb"
    "E2sg2sGA4wYA+MajyyYiyvc82PMGqiGDAeEGAPjCwwGkCaohmUCoBADgib7+/p0eDiCJaCM8cuDA"
    "gRch2jzAcQMAhPHjsht1oK9M4LgBADXxmOZnUhkzVku0R0ZGtwVfZeMAxw0AcMXHASSRh8KakZHR"
    "bXDj3oDjBgDY4jXNz4KwaOdyue2Li/+X8r/KxgSOGwBwDx76jNyFpmljmzen5kVEu6+/fycREVID"
    "vQPhBgDchY8DSJN8Z2fneyKFNdls1yAREYpw/IFQCQCAiPyl+VnI7+rbdUZUtIvFxTRE2z9w3AAA"
    "vweQJsKzIbPZrsEbN248gBauwYBwA9DACI4Tc0O4GjKdTu9fXi6l9+7de9LHfYCFpvX19ajXAACI"
    "gKAu20thTUvLpkO6rrei5J0HCDcADUiAA0giojwR0fp6+XmRbzZFWzScAmoD4QaggbCk+REFcNqi"
    "MWpTtDHlhhfEuEFsKR0dzHBdK/Xc+Tmua6lKQJdN5LEa8pVXXhmFaMsBjhvEktKRh3dQIrlGRLMM"
    "l8sSESVSW0v3HTx9k+F6SsFwAEnksRpyevrsXxLRuKZpY8gg4QeOG8QZDtGuXKe8VOhemRymehLv"
    "gAeQROStGtIq2kSURwaJHFCAA4BJInm1vFRoXZkc7oh6KUEJ0GekmnxnZ+d7oiXsVtHe1bfrDJpH"
    "yQGOG8SSxJa2Ynmp0E2J5FXeCyevlpcK3UQUW9ftt8+IDcKFNVX3zGcymTeRQSIPxLhBbFmZHO4o"
    "LxVa2cWbKEvl1ebUoQvvM19XOgwHkCaeqiEtzl44Fg78g1AJiC33HTx9kxLJNSqvdjNfepYSybXS"
    "kYd3MF9XGgH7jFST37Pn8RN+RFvTtCJEWz5w3CD2WNICuQ4rTbJE6qcKcrpsTdOKAwO7z4iWsFfd"
    "Ny9alAOCAccNYk/qufNzVF5tJkNoGZkl4s0X58TnODEnKoU1fkV7z57HTwRcAxAEjhvUDUZuN3e8"
    "m4goq1qON0eanwVf1ZCWewvHwwEPcNygbkhsaStKiHcTEc2qlCaYTqf3qyTayCAJHwg3qBvuO3j6"
    "pjTxNnK82a/rgb7+/p1NTYnDTKERIssUdpFvthPt9va2WQxECB8IN6grJGaaUJSZJul0er8lT5pF"
    "tDOZzJui1ZA2ok3IIIkOCDeoO1LPnZ8z+pjwH1YmkmthHlYyH0Ca5DOZzJsiTtmshtR1faLq/ihn"
    "j5C6OZw0J0bLwm8ML5fLbb/129+2Rr0OVeD8OW378peLbhkQzI2orISSJsh8AGniSbQdKjCFp94A"
    "OdSFcDPmsdqiadqYaG6rHU1NicPE9Hgb59P7qgZEQckfOHDgxVq9MKSJd3m1mxLJNRnibW2JSsyi"
    "7bOE/a5riAo/kEfshZtZDBwJ0p6S0znFuU2mESedYLiUJ/GQmSZIxOu8JblsIg8u2WUNEG1FiH2M"
    "++233/4mSRZtIiJd11v9PubPzn5wXtO0YtTriJK+/v6dhoNkwYt4yEwTJNromcJxMeY0PyueBvo6"
    "ibamaUWIthrEWrj7+vt3GiGSMBj/8Nq1+/2+uLOz8z0yZvUFXYdl9FRsePfX736HGLMhvLygkmnC"
    "f1hJRDRbLi2mgog3c58RK3lN08YOHDjwos9qyApecr2BfGIt3IxiIMTCQiGbzXYN+nktp+sm2nic"
    "5bqWbDjdtl/XZwlnSBNvPy800/xssjaCUimsEemJXeOcCBkkihFb4eZ+9BZk/MaNGw/4fXHPgz1v"
    "EJPrDrKOsOF028Z76AuJPU2IyIilC2IOOpB1qO7FIdcSbQxEUI/YCnfYbttE1/VWv2734szMZc5Y"
    "dxxcdzbbNcjptoNm1KQOXXhfWkMqDwU6RtYIt8s2Ed7gamweKGdXlFgKN6cY+GDcOLzxxcDA7jPU"
    "QK7bWGPkbtuKRby5ESrQyeVy22V/fkXE1q4a0grK2dUllsIt6eTdE+l0er+f101NTV1vb29jySlW"
    "3XWr5ratyM40cRNvzoIsv1h+No6/R62tW+fDWxHwQuyEWxGhGl9YKGRHRka3+Xlxb2/vW8TkuoO4"
    "f9lwdrAznlTYkNrThGiWyqvNTpkmYYQeaqWMdnVla+aeF4uLab4VAU5iJ9wquG2D8XPnXn3Mzws5"
    "XTeRf/cvE84Ntr29bVZGebXEniY1J8YbKY0cm7cdNVNGp6amru/q2+UatguSRQXkEivhVk2gFhYK"
    "2Vwut93Pax999LFXicl1B3H/suCsFDWeUKQgNdPEpRXs7OwH543NW4p4a5pWbGnZdMjtey7OzFyu"
    "sYGMz83NfSuOBV/1TmyEO5fLbZfZj8Qn46+99rqvYphTp07eYvzF9e3+ZcC5wW7enJqX3cxIYqaJ"
    "ayvY+fn5l2WJt67rE7qut9b6WQhsIOOXLl4a8mtQgBxiI9ycpe27+nZRe3sbx6UClaBz9jJWxXWP"
    "jIxu42z0bzyZSCeqTJP5+fmXOQuzqhhfXi6la4U7BDaQcaMfEFCEWAi3xW0HJpPJPH1xZqZp+Ac/"
    "+GOO6xHRuJFT7nc9XLFOJVy3sQa26SxhFn5ElWmyd+/ek5qmjUm4L+m6PiES7hDZQGqFXkB4xEK4"
    "jXAER7yUHnn0kVeJiH527NhvMpnM04EXR8HS8jjzZIPE3DmwuO3ARDFdRXZPEyJ78T516uQtxvx+"
    "O8bf/fW736n12aixgYyLhF5AOCgv3Jyl7Z2dnU//7Nix35h/f2LoiV9omnac4dKB0vI4XbffmDsH"
    "nG7baMoVOrJ7mjilCYpkeQRB1/WJWp8NgQ1kHJkmaqC8cHOVtmuadvyJoSd+Yf1v+cOHP+3s7LwS"
    "9NomKjSg0nW9NQrXzRnOIuJ9EvFKGJkmduItkOURCF3XW2uFOwQ2EGSaKIDSws3stq/kDx/+tPq/"
    "79u37zSn6/Z7QMjZgCoK1814eOy5basMJGeauKYJShRvoXCHSJogMk2iRWnh5nTb+/btO233tRde"
    "eL7Q82DPhaD3MPB9QMjZgIpI/gzO6ntxxrZV6Y8hMdPENU1Qco63UKaJwAaCTJMIUVa4OftcdHZ2"
    "XnnhhecLTl8femLodSbXHeiAkMt167o+ESTTxSuqtG2VQWJLW5Fkxbtr5HgbG7mUHG+RcIfIBoJM"
    "k2hQVrgZK++OP/XUU//g9j3PPvtMkdN1+w1VXJyZuczZgCoM1809JEG1FqL3HTx9U5rrNsTb6Yt3"
    "7tw+IjPHWyTTpMYGgkyTiFBSuDk/CD0P9lx49tlnirW+78ejo7/kct1BRJOzAVUYrpvTbXM3kooF"
    "NTYFmWmCIpkmRBsbSHt722x7e9sBm/+x9dwB4iSjXkA1nJV3mqYdH3pi6HWR733yySdvT09PvzI9"
    "ffavgt6XNkSzSESe3ePU1NT1dDo9u7DgGNnxRDbbNSgrZszttmWXtseRqamp67lc7sT09FkiCe0e"
    "TMdcK2c+7Jx64I5yjpsxF1jYbZv8aN++mfb2tp9y3DuI6+ZqQKXr+oTMYQuN4LZLRwczbuGMAGSp"
    "vNptxNBdmZqaui4z02RhoZBFuCNeKCXcnLnAmqYd//Ho6C+9vOb7Q0Nf9Pb2/orj/hQgVMHZgErW"
    "sAXOw2NZbVuDsjI53GGEMrjDAVkqrzanDl14/76Dp2+KvEB2miAKa+KFUsLN2Uiq58GeC08++eRt"
    "r6/765/85D84XbffXwbGR1MpI844R5KF1UjKC6Wjg5nyUqGVEsmrrBc2eqGkDl143+tLZacJorAm"
    "Pigj3My5wJ7dtsnA7t3lRx99jOuxXYlSeG7XzeW2NU0bC7uRlAiVfiK8op0lomxiS1vRUlbvGZlp"
    "gmQU1qjQZRK4o4xwc05t9+u2TX74Fz/8by7XTeQ/S4axFJ51xBmX29Z1vVW1Qy9LEyi+8Ijpsp87"
    "PycaGnFDdprgSy+99KykawMmlBBu5uwE327bhNt1Ly+X0n6LcoxmSyzuiuMAijG2rURpuxUJol05"
    "gAzisu2Q2QqWCIU1qqOEcHO67YGB3a8Ecdsmp06d/C/Gtq8TRvzeM5yum2PYAmNhlDKl7URElgpG"
    "HtG2xLI5XHY1klvBorBGcSIXbs7sBE3Tjv9o374ZjmsRUaV3NwcqlMJTwGELXHFyTdPGomrbakfp"
    "yMM7jJQ/DtGW5rKrkdwKFpkmChO5cDNmJ9DAwO5Xvj809AXHtYh4hy1QwFJ4rpimX9c9MjK6jctt"
    "E0XbttWKBNH2lOYXFMmtYJFpoiiRCjdzLvBPOd22idHD++cc1wpSlMP4WOzLdXMOSVChkdTK5HAH"
    "u2iTvzS/oMhOE0QLV/WITLi5HVxvb++vON22Sf7w4U8zmczbTJfzXZQzNTV1ndN1e/lF5B5JFnUj"
    "qZXJ4Q5LjnZQ0d4IjaS2lmSHRtyQOTGeIp6sBO4lMuHmLG1vb28jGW7bxBi2wHKtIDnVnK7by2Ep"
    "p9uOurS9SrSDIfkA0iuSW8HWnJ4DwiOSJlOcDo6IaHm5RMeOHfvusWPHuC55F7cKt77CeLnxGzdu"
    "FInIc4yXswGV6bprlZpztiGIurS9dHQwQ+XVZgbRzlJ5tTmxpa2ogmBbuXPn9pGWlk2HdF3nvvS4"
    "rut5kYZUQD5N6+vrod80nU7vX1govBT6jRVB07SxzZtT835+AUZGRrcZBRIcKXljd+7cPuL2PYw/"
    "q/yePY+fiEq4uUU7ili2KLlcbrsxnYa9myAZ+feqHC43KqGHSjhL2+OKrusTfrM7uBtQuR2W1ovb"
    "ZithD9BnJExkpwki0yR6QhduzmKbmOM7p5qzAZXbYalxIBXrRlJM1ZAsfUbC5OLMzGWZ4o1Mk2gJ"
    "Vbg5S9vrgSBFOZwNqOzcE+PPKh9VIymWakjmPiNhIjvHG8OCoyPUGLdxaDIR2g1jgEic2Qmu99Nu"
    "DYw/q/z6evl5hut4giFHW9kDSK8Y5xQsU6WqyGuaVvT7+QX+Cc1xcxbb1BNBinK4GlBVr4HTbUfR"
    "SIpFtEmdNL+gSMzxHtd1vRVtYMMnNMcNt22PkR8euesmI+uDaCO2LcvJy8SSo+1XtOvGZdthfFZa"
    "idd5R/JE1eiEkscNt+2MkW/b6neob8+DPW9cungpT8F/Gcenp8+y/kKH2UiKobBG+TS/oNy5c/tI"
    "Op3ev7xcGmMQ8DxR5awFhEwojrupKXGYkEniigqxbk7CdNssok0bB5CMy1IajvCGapOLGgnpjhs9"
    "fcUwS+Ejdt1chNZIKmBhjRkaKdVjaMQNiG68kSrcltJ2VQRFZcbn5uaIfJTCX5yZuZxOp+/nKIXn"
    "IKxGUoEKa8qr3ZRIKl9MA4AdUoWbs5EUGalHTNdihfPAx28viN7e3remp8+q4LpDaSQVoLCmrg8g"
    "QWMgTbg5y6WJKL+rb9eZqNuBOpHNdg0abjnwAeHycmlMpPlTNZwNqIIQRml7UNGGywZxR1oeN2O5"
    "tBI9nN1gnAsZaD6lUVYuo0pOlHxvb+9bMm/gsxrydz2zIdqgDpAi3Myl7ZH3cBaBcS4kLSwUsn6K"
    "cjgbUPlBttv2WVgT+jgxAGQjRbg5G0lF3cNZFM65kBRgUk6EvZKlNpLyJdox6eYHgFfYhZvbbct+"
    "9OaE03UHKYWX2FjICWmNpHzOhgxt0joAUcBegMNZDNLe3nYgbtM2OP/9QYpYQi56klL27LOwRmox"
    "jSXGHg4bGxYRif+bKu9blCSSa9XrreTch7gG8/+Kvnehr9EFt8wn1qwS5tL2WLltk4GB3Wemp8+2"
    "EoNoBinKyWQybzJlutRCSiMpH6IdXjENx7xK72RLRx7eIZLGyDZT0y/l1W5boeSZQORrPaUjD+8Q"
    "CplFtcZ719Ht9nNmDZVwTm2PS2y7mqmpqevGASEH48Z76hnOTBeRe3Fez69oyz6AtKQhRsEsJZJX"
    "aznplcnhjpDW40TW6nRNIl1XInmVEsm1Wk9LK5PDHXZrjwDb99AKm3D7nVxuh6ZpY3F02yacaXma"
    "phX9tg3gjLnboWnaGLfbLh0dzHgWbZJ/ALkyOdyhhBtLJNfcNhAF3HaznduOfF0bG9+a2wZibIpc"
    "pisQtUI7LKGSkZHRbYxuO795c2o+jm7b5NSpk7fOnXt1dmGhELiSUdf1CV3X8yMjo9u8Hv5dnJm5"
    "3NKy6TsSJn5X4HTbHvuOhNpnpFxaTNmuq7wq54YJx1/NWTI2q2pcRCkbZdzW1cnKeP9c3rtyaTFL"
    "RPd8XirvnZGJ5OFeTofmQd7zmq9jEe5rH177quG8WNxXPUyQnp+ff9l4CmF5T659eO2rROQ5a2Ng"
    "YPeZDz6YldJetasry3YA6KnvSMh9Rixuu3odV5q/9sAbzR07/p3rXusrxa+s3Xj38fJS4TEXAbLF"
    "wdWG8kTihu26yquU2NL2L82dPeea7mv9X477rK8Uv1JevplZ+/i9b1Mi+ZCX1xqbv2cD4Pj0I7lC"
    "l0W4Va5qjBIVNiDjyUXpp5dK7LG2aEfSZ8TpMT+xpe3jTX/+4jPc91v96J2//+y1o78olxbthkl7"
    "c9sRl/i7hSaaO3vOaY+MnZBwz38uLxUestlouxNb2kqsN7Pb0DcGS/Pep4pQBikA4IRwjvbGI2zo"
    "IuT4mF9evdLc2XNWxj2TX3/o889bO67RUuHex34HIXZ02x5dOzeOIaZE8mKy609DT/Xl3PDdNkvZ"
    "xgLCDSJDULQj7ebn8pj/sfbI2N/Kuu968eY3REVXabdtH2Ki5q89cCn59Yc+577nF/9z7o/KpcW0"
    "nQvm3sQcNqVQNksINwgdD7MhI+3m5/KYfyW548/+TtZ99X+beKq8VPia6CO4i6uNNLXNZV30e90D"
    "x7nvt/rRO1/6/NJLE1Re7RN9UgmE/aYUyucVwg1CRThHW4FBB25u+/e/efBfZdzzs7cmv/vFlQsH"
    "KZH8k6ovZYnufdR3dLXWr0tA6OnHwW0ntrRR0x9s+4RrLasfvfOltU8uD6y+/6vR8lLhew6x7SLX"
    "/YiMQ8kIN0YINwgNQdFWYtCBWwqbDLe9+tE7X/r8P38+sfbJ1W8RUXWPGscyfkdXu8FsubTIvNLK"
    "elx/No7ClkhSubRIn7129B/vlBbTidTW+TLDnxWX7SDa7J8l+7RV6YeSJhBuEApCOdoKuOzKUpw2"
    "mESS1m6+/+3b//Tst7nutV68+Y1yabGDyqs7bWOzDo/ftdy2FEQzM2r8rMulxe8ZfxLHn7bvgSTR"
    "jvJQ0gTCDaQjINpKuGwT18fg8iqtffze30gRSzvRJucc7BpuWxq1fkZRhxHIeN9kFWepkMED4QZS"
    "ESisUW+cmNsmE84vZ9Z00q6lz9G47aLA90XVGkDsfZNByJ9hCDeQhsBsyMir+qqJ3C0K5qs7rPOe"
    "4pxEamupXFpMsfw9kVTPbVtK1MNofxD558MAwg2kUCNHO9Q+I56Ixi2aTnFN+D2xW6ez66u+XtC/"
    "e1uXZUMxNwLRP42XOW78oX+G7N939qyVWkC4ATuuoq3QAWQ1jm7Ka+MhLySSa4nUVk/i4+i2I66S"
    "9FAIdFP0T7dOiF7ft6C4ue2wDQiEG7DiItpKHUDa4uKmlFqzN7cdGg55791BQguJ1NZSeanQbfcU"
    "ZLRhjdZth5gCaEXKsGDQeLjOhrQM7VVKAC24uNg1ldbskh8dadzVrdAnyEGh63tfo782JyqkAFqB"
    "cIPAVBXWWEU7PkN7N3onV284tkMBIsV+nZRIbQ3d9d21BOcUueAbysY17LoizloPUmUi9d/nA4RK"
    "QCBcqiHVS/NzQNWYcTU1qhFTK5PDoazDtuzeAY6NL/Xc+Tnjae7eL0Y52DfCz7dan0wQKxwLaxQ+"
    "gKzGcSSZipuOe8bLbHmpIHsFttkTbgMcpGOMcpP5ZKRKCqAVCDfwhYNoq38AWYUKVXAiCImH/DWL"
    "x/uZN77ElraiwyGl4yg3NhQ6lDRBjBt4xla0Y3AAWY1r+locYtvh3r/bLo4e1mFprc+UrENKl0Ea"
    "kRxKmkC4gSdsRDs+B5BVqHbg5IQqj+q2QmW/oWSlHJY6vwezRmogOw6T3yP/jKj1PAiUppLud7do"
    "qxcLFsBlqrd6/57fHcDJKwSqgV1su1IcY/MeynCjlZxuB1YmhzukjCZT8DPStL6+HuX9QUywydF2"
    "7BENAJALHDeoSZVoq9tnBIAGAcINHLlnNmSM0vwAqGcQKgG2VBXWxC7ND4B6Bo4b3MNdog2XDYBy"
    "wHGDu7grPAKXDYCSQLhBhUqOtgFcNgBqglAJIKK7xowRJZJrSPMDQF0g3MBaSIHQCAAxAMLd4FhK"
    "2NcQGgEgHkC4G5jSkYd3EG2UM8NlAxAfINwNiinacNkAxA8IdwNilrDjABKAeALhbiDMHG2ERgCI"
    "NxDuBmFlcrijXFpMITQCQPzBIIUGwEz3Q2gEgPoAjrvOkT1IFQAQPih5r2O4J4IAANQAwg0AADED"
    "MW4AAIgZEG4AAIgZEG4AAIgZEG4AAIgZ/w94963Tgg0YxgAAAABJRU5ErkJggg=="
)

# Thông tin phiên bản và bản quyền
SOFTWARE_INFO = """
PDF Processing tools
Công cụ xử lý PDF
---
Phiên bản: 2.10
Phát triển bởi: Anhtn
Tháng 09 năm 2024
Bản quyền thuộc về avxpert.vn
--------------------------------
CÔNG TY CỔ PHẦN AVXPERT VIỆT NAM
Địa chỉ:Số 6 Ngõ 110, Đường Mỹ Đình, Phường Mỹ Đình 2, Quận Nam Từ Liêm, Thành phố Hà Nội, Việt Nam.
Điện thoại:0982192076
Email:info@avxpert.vn
"""

GUIDE_INFO = """
Hướng dẫn sử dụng Chức năng Highlight PDF:
1. Chọn file PDF bằng cách nhấn nút "Chọn file PDF".
2. Nhập các từ khóa cần tìm (mỗi từ khóa trên một dòng).
3. Nhấn nút "Tìm kiếm nội dung" để tìm từ khóa trong file PDF.
4. Kết quả sẽ hiển thị số lượng từ khóa tìm thấy.
5. Bạn có thể nhấn vào từ khóa để xem vị trí từ khóa đó trong PDF.
6. Nhấn nút "Lưu file đã tô màu" để lưu file PDF đã tô sáng từ khóa.
"""

# Biến toàn cục
pdf_path = None
doc = None
current_page = 0
pdf_images = []  # Lưu trữ hình ảnh của các trang PDF để hiển thị
save_folder_path = None  # Đường dẫn thư mục để lưu file PDF đã tô màu
keywords_found = False  # Biến toàn cục để lưu trạng thái kết quả tìm kiếm
original_doc = None  # Biến để lưu bản gốc của file PDF
selected_files = [] # Khai báo biến toàn cục để lưu danh sách các file đã chọn

# Hàm chuyển giao diện - sử dụng pack_forget để ẩn frame hiện tại và pack để hiển thị frame cần thiết
def switch_frame(frame_to_show):
    for frame in [welcome_frame, pdf_frame, under_development_frame, remove_highlight_frame]:
        frame.pack_forget()  # Ẩn tất cả các frame
    frame_to_show.pack(fill="both", expand=True)  # Hiển thị frame cần thiết

# Giao diện chính - Welcome Frame
def show_welcome_frame():
    switch_frame(welcome_frame)

# Giao diện làm việc với PDF - PDF Frame
def show_pdf_frame():
    switch_frame(pdf_frame)

# Giao diện làm việc với Remove Highlight PDF Frame 
def show_remove_highlight_pdf_frame():
    switch_frame(remove_highlight_frame)

# Hàm để thoát ứng dụng
def exit_app():
    root.quit()

# Hàm hiển thị thông tin ứng dụng và logo
def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("Giới thiệu")
    
    # Đặt kích thước cố định cho cửa sổ giới thiệu
    window_width, window_height = 700, 400  # Điều chỉnh kích thước theo yêu cầu (rộng x cao)
    about_window.geometry(f"{window_width}x{window_height}")

    # Tính toán tọa độ để cửa sổ xuất hiện ở giữa màn hình chính
    root_x = root.winfo_x()
    root_y = root.winfo_y()
    root_width = root.winfo_width()
    root_height = root.winfo_height()

    # Tính toán vị trí (toạ độ) giữa màn hình
    position_right = int(root_x + (root_width / 2) - (window_width / 2))
    position_down = int(root_y + (root_height / 2) - (window_height / 2))

    # Đặt vị trí của cửa sổ giới thiệu vào giữa cửa sổ chính
    about_window.geometry(f"+{position_right}+{position_down}")

   # Sử dụng Frame để dễ dàng bố cục các phần tử
    about_frame = tk.Frame(about_window)
    about_frame.pack(expand=True)

    # Giải mã Base64 và hiển thị logo
    try:
        logo_data = base64.b64decode(image_base64)
        logo_image = Image.open(io.BytesIO(logo_data))
        logo_image = logo_image.resize((366, 182), Image.Resampling.LANCZOS)  # Điều chỉnh kích thước logo nếu cần
        logo_tk = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(about_frame, image=logo_tk)
        logo_label.image = logo_tk  # Lưu tham chiếu để tránh bị xóa khỏi bộ nhớ
        logo_label.pack(pady=10, anchor="center")  # Căn giữa logo
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải ảnh logo từ Base64: {e}")
    
    # Thông tin phần mềm
    info_label = tk.Label(about_frame, text=SOFTWARE_INFO, justify=tk.CENTER)  # Căn giữa đoạn văn bản
    info_label.pack(padx=20, pady=20, anchor="center")

    # Nút đóng cửa sổ
    close_button = tk.Button(about_frame, text="OK", command=about_window.destroy)
    close_button.pack(pady=5, anchor="center")

    # Đặt cửa sổ ở chế độ modal
    about_window.grab_set()  # Ngăn người dùng tương tác với các cửa sổ khác cho đến khi đóng cửa sổ này
    about_window.transient(root)  # Đặt cửa sổ này luôn nổi trên cửa sổ chính
    about_window.wait_window(about_window)  # Chờ cho đến khi cửa sổ này bị đóng

# Hàm hiển thị hướng dẫn sử dụng
def show_guide():
    messagebox.showinfo("Hướng dẫn", GUIDE_INFO)

# Hàm hiển thị thông báo chức năng đang phát triển
def show_under_development():
    switch_frame(under_development_frame)

# Hàm chọn file PDF
def open_pdf():
    global doc, pdf_path, current_page, pdf_images, original_doc
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        doc = fitz.open(pdf_path)
        original_doc = fitz.open(pdf_path)  # Lưu lại bản gốc của file PDF
        current_page = 0
        pdf_images = convert_pdf_to_images()  # Chuyển đổi các trang PDF thành hình ảnh
        display_pdf_page(current_page)
        result_text.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô kết quả
        if len(doc) > 1:
            prev_page_button.pack(side=tk.LEFT, padx=20)  # Hiển thị nút Trang trước
            next_page_button.pack(side=tk.LEFT, padx=20)  # Hiển thị nút Trang sau
        else:
            prev_page_button.pack_forget()  # Ẩn nút Trang trước
            next_page_button.pack_forget()  # Ẩn nút Trang sau

# Hàm xử lý khi kéo thả file vào khu vực chọn file
def on_drop(event):
    global pdf_path, doc, current_page, pdf_images, original_doc
    pdf_path = event.data.strip('{}')  # Xử lý chuỗi đường dẫn từ sự kiện
    if pdf_path.lower().endswith('.pdf'):
        doc = fitz.open(pdf_path)
        original_doc = fitz.open(pdf_path)  # Lưu lại bản gốc của file PDF
        current_page = 0
        pdf_images = convert_pdf_to_images()  # Chuyển đổi các trang PDF thành hình ảnh
        display_pdf_page(current_page)
        result_text.delete(1.0, tk.END)  # Xóa nội dung cũ trong ô kết quả
        if len(doc) > 1:
            prev_page_button.pack(side=tk.LEFT, padx=20)  # Hiển thị nút Trang trước
            next_page_button.pack(side=tk.LEFT, padx=20)  # Hiển thị nút Trang sau
        else:
            prev_page_button.pack_forget()  # Ẩn nút Trang trước
            next_page_button.pack_forget()  # Ẩn nút Trang sau
    else:
        display_message("Vui lòng thả tệp PDF hợp lệ.")

# Hàm chuyển đổi PDF thành hình ảnh
def convert_pdf_to_images():
    images = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    return images

# Hiển thị trang PDF với kích thước ưu tiên chiều rộng
def display_pdf_page(page_num):
    if not pdf_images:  # Kiểm tra nếu chưa có hình ảnh PDF
        return
    img = pdf_images[page_num]
    canvas_width = pdf_viewer.winfo_width()
    img_ratio = img.width / img.height  # Tỷ lệ chiều rộng / chiều cao của PDF
    new_width = canvas_width
    new_height = int(canvas_width / img_ratio)  # Điều chỉnh chiều cao để giữ tỷ lệ
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(resized_img)
    pdf_viewer.create_image(0, 0, anchor="nw", image=img_tk)
    pdf_viewer.image = img_tk

    # Cập nhật vùng cuộn của canvas theo kích thước hình ảnh
    pdf_viewer.config(scrollregion=(0, 0, new_width, new_height))

# Chuyển trang PDF
def next_page():
    global current_page
    if pdf_images and current_page < len(pdf_images) - 1:
        current_page += 1
        display_pdf_page(current_page)

def prev_page():
    global current_page
    if pdf_images and current_page > 0:
        current_page -= 1
        display_pdf_page(current_page)

# Lấy từ khóa từ ô nhập liệu
def get_keywords():
    raw_keywords = keyword_entry.get("1.0", tk.END).strip()  # Lấy toàn bộ nội dung từ ô nhập liệu
    keywords = [kw.strip() for kw in raw_keywords.splitlines() if kw.strip()]  # Mỗi từ khóa là 1 dòng, bỏ trống các dòng không có từ khóa
    return keywords

# Tìm kiếm từ khóa và highlight chúng trực tiếp trong PDF Viewer
def search_keywords():
    global doc, keywords_found
    doc = fitz.open(pdf_path)  # Tải lại file PDF từ đường dẫn gốc

    if not doc:
        display_message("Vui lòng chọn file PDF trước!")
        return

    # Lấy từ khóa và loại bỏ khoảng trắng thừa
    keywords = get_keywords()
    if not keywords:
        display_message("Vui lòng nhập từ khóa cần tìm!")
        return

    found_keywords = {}
    for keyword in keywords:
        keyword_cleaned = keyword.strip()  # Loại bỏ khoảng trắng thừa
        if not keyword_cleaned:
            continue

        found_keywords[keyword_cleaned] = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text_instances = page.search_for(keyword_cleaned)  # Tìm kiếm chính xác từ khóa

            # Highlight từ khóa trên trang
            if text_instances:
                for inst in text_instances:
                    page.add_highlight_annot(inst)  # Thêm highlight cho từ khóa
                found_keywords[keyword_cleaned].append(page_num)

    if any(found_keywords.values()):
        keywords_found = True
        pdf_images[:] = convert_pdf_to_images()  # Cập nhật các hình ảnh PDF sau khi đã highlight
        display_pdf_page(current_page)  # Hiển thị lại trang hiện tại với highlight
        display_search_results(found_keywords)
    else:
        keywords_found = False
        display_message("Không tìm thấy từ khóa trong PDF.")

# Hiển thị kết quả tìm kiếm
def display_search_results(found_keywords):
    result_text.delete(1.0, tk.END)
    total_keywords = len(found_keywords)
    found_count = sum(1 for pages in found_keywords.values() if pages)
    result_text.insert(tk.END, f"Tìm được {found_count}/{total_keywords} từ khóa.\n\n")

    for keyword, pages in found_keywords.items():
        color = "blue" if pages else "gray"
        result_text.insert(tk.END, f"Từ khóa: {keyword} - ", color)
        if pages:
            for page_num in pages:
                result_text.insert(tk.END, f"Trang {page_num + 1} ", "link")
            result_text.insert(tk.END, "\n")
        else:
            result_text.insert(tk.END, "Không tìm thấy\n", "gray")

    # Sự kiện nhấp vào từ khóa
    def click_link(event):
        index = result_text.index("@%s,%s" % (event.x, event.y))
        tag_ranges = result_text.tag_ranges("link")
        for i in range(0, len(tag_ranges), 2):
            if result_text.compare(tag_ranges[i], "<=", index) and result_text.compare(tag_ranges[i + 1], ">=", index):
                page_num = int(result_text.get(tag_ranges[i], tag_ranges[i + 1]).strip().split(" ")[-1]) - 1
                display_pdf_page(page_num)

    result_text.tag_bind("link", "<Button-1>", click_link)

# Hàm lưu file đã tô màu
def save_highlighted_pdf():
    global save_folder_path

    if not doc:
        display_message("Vui lòng chọn file PDF trước!")
        return

    # Kiểm tra nếu không có từ khóa nào được tìm thấy trước đó
    if not keywords_found:
        confirm_save = messagebox.askyesno("Cảnh báo", "Không có từ khóa nào được tìm thấy và tô màu. Bạn có muốn lưu file không?")
        if not confirm_save:
            return

    base_name, ext = os.path.splitext(os.path.basename(pdf_path))  # Lấy tên file gốc (không có thư mục)
    if save_folder_path:
        save_path = os.path.join(save_folder_path, f"{base_name}_Highlighted{ext}")
    else:
        save_path = f"{os.path.splitext(pdf_path)[0]}_Highlighted{ext}"
    
    doc.save(save_path)
    display_message_with_link(f"File đã được lưu thành công. Nhấn vào đường dẫn dưới để mở file:", save_path)

# Hàm Undo để tải lại file PDF gốc chưa bôi màu
def undo_highlight():
    global doc, pdf_images, current_page
    if original_doc:
        result_text.delete(1.0, tk.END)
        doc = fitz.open(pdf_path)  # Tải lại file PDF từ bản gốc
        pdf_images = convert_pdf_to_images()  # Chuyển đổi các trang PDF thành hình ảnh
        current_page = 0  # Quay lại trang đầu tiên
        display_pdf_page(current_page)
        display_message("Đã hoàn tác thao tác tô màu. PDF đã quay về trạng thái gốc.")
    else:
        display_message("Không thể hoàn tác, vui lòng mở file PDF trước.")

# Hiển thị thông báo
def display_message(message):
    messagebox.showinfo("Thông báo", message)

# Hàm mở file PDF trong trình đọc mặc định của hệ thống
def open_pdf_in_system_viewer(file_path):
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)  # Windows
        elif platform.system() == "Darwin":
            subprocess.run(["open", file_path])  # macOS
        else:
            subprocess.run(["xdg-open", file_path])  # Linux
    except Exception as e:
        display_message(f"Không thể mở file: {e}")

# Hiển thị thông báo với đường dẫn có thể nhấp chuột
def display_message_with_link(message, file_path):
    msg_window = tk.Toplevel(root)
    msg_window.title("Thông báo")
    msg_label = tk.Label(msg_window, text=message)
    msg_label.pack(pady=10)

    link_label = tk.Label(msg_window, text=file_path, fg="blue", cursor="hand2")
    link_label.pack(pady=10)

    def open_file(event):
        open_pdf_in_system_viewer(file_path)

    link_label.bind("<Button-1>", open_file)
    close_button = tk.Button(msg_window, text="Đóng", command=msg_window.destroy)
    close_button.pack(pady=5)

# Hàm thay đổi thư mục lưu file PDF
def change_save_folder():
    global save_folder_path
    folder_selected = filedialog.askdirectory()  # Mở cửa sổ chọn thư mục
    if folder_selected:
        save_folder_path = folder_selected
        display_message(f"Thư mục lưu đã thay đổi: {save_folder_path}")
    else:
        display_message("Không có thư mục nào được chọn.")

# Sự kiện cuộn chuột để cuộn nội dung PDF trong Canvas
def on_mouse_wheel(event):
    if event.delta:
        pdf_viewer.yview_scroll(int(-1*(event.delta/120)), "units")

# Hàm chọn nhiều file PDF
def select_multiple_files():
    global selected_files
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if file_paths:
        selected_files[:] = file_paths  # Cập nhật danh sách file đã chọn
        file_listbox.delete(0, tk.END)  # Xóa danh sách cũ trong listbox
        
        # Hiển thị đường dẫn thư mục chung
        directory_path = os.path.dirname(selected_files[0])
        file_listbox.insert(tk.END, f"Đường dẫn thư mục: {directory_path}")
        file_listbox.bind("<Double-Button-1>", on_file_click) # Liên kết sự kiện nhấp chuột với file_listbox để mở file hoặc thư mục

        # Hiển thị tên ngắn gọn của các file đã chọn
        for file_path in selected_files:
            short_name = os.path.basename(file_path)  # Lấy tên file (không bao gồm đường dẫn)
            file_listbox.insert(tk.END, short_name)
        
        # Hiển thị thông báo về số lượng file đã chọn
        number_of_files = len(selected_files)
        file_listbox.insert(tk.END, f"\nBạn đã chọn {number_of_files} file PDF.")

    else:
        display_message("Không có file nào được chọn.")

# Hàm thực thi xóa highlight cho các file đã chọn
def execute_remove_highlight():
    global selected_files
    if not selected_files:
        display_message("Vui lòng chọn ít nhất một file PDF.")
        return

    cleaned_files = remove_highlight_from_files(selected_files)

    # Hiển thị kết quả trong file_listbox
    file_listbox.delete(0, tk.END)  # Xóa danh sách cũ

    if cleaned_files:
        # Lấy đường dẫn thư mục chung
        directory_path = os.path.dirname(cleaned_files[0])
        file_listbox.insert(tk.END, f"Đường dẫn thư mục: {directory_path}")
        file_listbox.bind("<Double-Button-1>", on_file_click) # Liên kết sự kiện nhấp chuột với file_listbox để mở file hoặc thư mục

        # Hiển thị tên ngắn gọn của các file đã làm sạch
        for file_path in cleaned_files:
            short_name = os.path.basename(file_path)  # Lấy tên file (không bao gồm đường dẫn)
            file_listbox.insert(tk.END, short_name)

        # Hiển thị thông báo về số lượng file đã xử lý thành công
        number_of_files = len(cleaned_files)
        file_listbox.insert(tk.END, f"\nĐã xóa Highlight thành công cho {number_of_files} file. File được lưu với dấu _ ở cuối tên file.")
    else:
        display_message("Không có file nào được làm sạch annot.")

# Hàm xóa highlight cho danh sách các file PDF
def remove_highlight_from_files(file_paths):
    cleaned_files = []
    
    for file_path in file_paths:
        try:
            # Mở file PDF
            doc = fitz.open(file_path)
            
            # Duyệt qua tất cả các trang và xóa tất cả các chú thích (annotation)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                annotations = page.annots()  # Lấy tất cả các annotations trên trang
                if annotations:  # Nếu trang có annotations
                    for annot in annotations:
                        page.delete_annot(annot)  # Xóa tất cả các annotations

            # Lưu file mới với hậu tố "_"
            base_name, ext = os.path.splitext(file_path)
            new_file_path = f"{base_name}_{ext}"
            doc.save(new_file_path)
            cleaned_files.append(new_file_path)  # Thêm file đã làm sạch vào danh sách kết quả
            doc.close()

        except Exception as e:
            display_message(f"Đã xảy ra lỗi khi xóa chú thích trong file {file_path}: {e}")

    return cleaned_files  # Trả về danh sách các file đã làm sạch

# Sử dụng lại hàm open_pdf_in_system_viewer đã có để mở file PDF hoặc thư mục
# Sử dụng lại hàm open_pdf_in_system_viewer đã có để mở file PDF hoặc thư mục
def on_file_click(event):
    try:
        # Lấy các mục được chọn từ Listbox
        selected_index = file_listbox.curselection()

        # Nếu không có mục nào được chọn, thoát khỏi hàm
        if not selected_index:
            return

        # Lấy mục được chọn
        selected_item = file_listbox.get(selected_index)

        # Nếu mục là trống, bỏ qua không thực hiện gì
        if selected_item.strip() == "":
            return

        # Nếu mục là đường dẫn thư mục, mở thư mục
        if selected_item.startswith("Đường dẫn thư mục:"):
            folder_path = selected_item.replace("Đường dẫn thư mục: ", "").strip()
            if os.path.isdir(folder_path):
                open_pdf_in_system_viewer(folder_path)  # Mở thư mục
        else:
            # Nếu mục là tên file, lấy đường dẫn thư mục từ mục thứ hai (không phải dòng đầu tiên hiển thị mô tả)
            folder_path = file_listbox.get(0).replace("Đường dẫn thư mục: ", "").strip()
            file_name = selected_item.strip()
            file_path = os.path.join(folder_path, file_name)

            # Kiểm tra xem file có tồn tại không trước khi mở
            if os.path.isfile(file_path):
                open_pdf_in_system_viewer(file_path)  # Mở file
    except Exception as e:
        pass  # Bỏ qua lỗi mà không hiển thị thông báo





# Tạo giao diện chính
# Khởi tạo root với TkinterDnD để hỗ trợ kéo thả
root = TkinterDnD.Tk()
root.title("PDF Processing Tools - V2.10")
root.geometry("1500x810")

# Menu chính của ứng dụng
menubar = Menu(root)
root.config(menu=menubar)

# Menu chức năng
mainmenu = Menu(menubar, tearoff=0)
mainmenu.add_command(label="1.Tô màu [Highlight PDF]", command=show_pdf_frame)
mainmenu.add_command(label="2.Xóa Highlight PDF", command=show_remove_highlight_pdf_frame)
mainmenu.add_command(label="3.Trích xuất thông số kỹ thuật [Extract form PDF]", command=show_under_development)
mainmenu.add_command(label="4.So sánh thông số [Text vs PDF]", command=show_under_development)

mainmenu.add_command(label="Thoát", command=exit_app)
menubar.add_cascade(label="Chức năng", menu=mainmenu)

# Menu Trợ giúp
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Giới thiệu", command=show_about)
helpmenu.add_command(label="Hướng dẫn", command=show_guide)
menubar.add_cascade(label="Trợ giúp", menu=helpmenu)

# Tạo Frame Welcome (Giao diện chào mừng)----------------------------------------------------------------------------
welcome_frame = tk.Frame(root)
welcome_label = tk.Label(welcome_frame, text="Chào mừng đến với Phần mềm xử lý PDF", font=("Arial", 23))
welcome_label.pack(pady=50)
welcome_desc = tk.Label(welcome_frame, text="Chọn chức năng từ menu để bắt đầu", font=("Arial", 14))
welcome_desc.pack(pady=20)

# Tạo Frame Chờ Phát Triển (Under Development Frame)----------------------------------------------------------------------------
under_development_frame = tk.Frame(root)
under_development_label = tk.Label(under_development_frame, text="Chức năng này đang được phát triển", font=("Arial", 23))
under_development_label.pack(pady=50)
under_development_desc = tk.Label(under_development_frame, text="Vui lòng quay lại sau!", font=("Arial", 14))
under_development_desc.pack(pady=20)

# Tạo Frame cho chức năng Xóa Highlight PDF-----------------------------------------------------------------------------
remove_highlight_frame = tk.Frame(root)

# Thêm hướng dẫn và nút để xóa highlight
instruction_label = tk.Label(remove_highlight_frame, text="Hãy chọn 1 hoặc nhiều file PDF đã tô màu để xóa highlight:")
instruction_label.pack(pady=10)

# Nút để chọn file PDF
select_files_button = tk.Button(remove_highlight_frame, text="Chọn file PDF", command=select_multiple_files)
select_files_button.pack(pady=10)


# Ô hiển thị danh sách file đã chọn
file_listbox = tk.Listbox(remove_highlight_frame, height=10, width=160)
file_listbox.pack(pady=10)


# Nút để xóa highlight trên các file đã chọn
remove_highlight_button = tk.Button(remove_highlight_frame, text="Xóa Highlight các file trên", command=execute_remove_highlight)
remove_highlight_button.pack(pady=10)


# Tạo Frame PDF (Chức năng tô màu PDF)------------------------------------------------------------------------------------
pdf_frame = tk.Frame(root)

# Thêm sự kiện kéo thả vào khung của ứng dụng PDF
pdf_frame.drop_target_register(DND_FILES)
pdf_frame.dnd_bind('<<Drop>>', on_drop)

# Tạo PanedWindow để chia hai khung trái và phải cho chức năng "Tô màu PDF"
paned_window = tk.PanedWindow(pdf_frame, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Khung bên trái chứa ô nhập từ khóa và kết quả tìm kiếm
left_frame = tk.Frame(paned_window)
paned_window.add(left_frame)


# Tạo một Frame cho nút chọn file và thêm hướng dẫn kéo thả
drop_frame = tk.Frame(left_frame, bg='#b3d9ff')
drop_frame.pack(pady=5)

# Nút chọn file PDF
open_button = tk.Button(drop_frame, text="Chọn file PDF", command=open_pdf)
open_button.pack(pady=5)

# Hướng dẫn kéo thả
label = tk.Label(drop_frame, text="hoặc kéo thả tệp vào ứng dụng", bg='#b3d9ff')
label.pack()

# Ô nhập từ khóa
keyword_label = tk.Label(left_frame, text="Nhập các từ khóa vào ô dưới (mỗi từ khóa trên một dòng):")
keyword_label.pack(pady=5, anchor="sw")

keyword_entry = ScrolledText(left_frame, height=10, width=80)
keyword_entry.pack(pady=5, expand=True, fill=tk.BOTH)

# Nút tìm kiếm từ khóa
search_button = tk.Button(left_frame, text="Tìm kiếm & Tô màu", command=search_keywords)
search_button.pack(padx=5, pady=5)

# Nút Undo để hoàn tác highlight
undo_button = tk.Button(left_frame, text="Hoàn tác tô màu", command=undo_highlight)
undo_button.pack(padx=5, pady=5)

# Ô hiển thị kết quả tìm kiếm
result_label = tk.Label(left_frame, text="Kết quả tìm kiếm:")
result_label.pack(pady=2, anchor="sw")

result_text = ScrolledText(left_frame, height=10, width=80)
result_text.pack(pady=10, expand=True, fill=tk.BOTH)
result_text.tag_config("blue", foreground="blue")
result_text.tag_config("gray", foreground="gray")
result_text.tag_config("link", foreground="blue", underline=True)

# --------------------------------------------------------------------
# Tạo một Frame cho nút Đổi thư mục và nút Lưu file
# drop_frame = tk.Frame(left_frame, relief=tk.RIDGE, bd=0)
# drop_frame.pack(pady=5)
drop_frame = tk.Frame(left_frame)
drop_frame.pack(side=tk.BOTTOM, pady=10)


# Nút để thay đổi thư mục lưu file
change_folder_button = tk.Button(drop_frame, text="Change folder to save", command=change_save_folder)
change_folder_button.pack(side=tk.LEFT, padx=5)

# Nút lưu file đã tô màu
highlight_button = tk.Button(drop_frame, text="Lưu file đã tô màu", command=save_highlighted_pdf)
highlight_button.pack(side=tk.LEFT, padx=5)

# Khung bên phải chứa PDF Viewer
right_frame = tk.Frame(paned_window)
paned_window.add(right_frame)

# Canvas để hiển thị hình ảnh PDF
pdf_viewer = Canvas(right_frame, bg="white")
pdf_viewer.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Khung điều hướng cho các nút chuyển trang
nav_frame = tk.Frame(right_frame)
nav_frame.pack(side=tk.BOTTOM, pady=10)

# Nút chuyển trang
prev_page_button = tk.Button(nav_frame, text="Trang trước", command=prev_page)
next_page_button = tk.Button(nav_frame, text="Trang sau", command=next_page)
prev_page_button.pack(side=tk.LEFT, padx=5)
next_page_button.pack(side=tk.LEFT, padx=5)

# Liên kết sự kiện cuộn chuột với canvas
pdf_viewer.bind_all("<MouseWheel>", on_mouse_wheel)

# Hiển thị giao diện Welcome khi khởi động
show_welcome_frame()

# Vòng lặp chính của Tkinter
root.mainloop()
