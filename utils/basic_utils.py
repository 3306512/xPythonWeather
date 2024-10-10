def validate(obj):
    try:
        f_obj = float(obj)
        # тут я загуглил рекордные минимальные и максимальные значения температуры воздуха,
        # если даже это недостаток, то его легко убрать
        if 56.7 > f_obj > -91.2:
            return True
        else:
            return False
    except ValueError:
        return False
