from . import retrieve_name_ex

tensor_type = ['Tensor', 'ndarray']

def tpr(var):
    var_name = retrieve_name_ex(var)
    var_type = str(type(var)).split("'")[1].split('.')[-1]

    if not var_type in tensor_type:
        out_str = '>>>\n' + f'{var_name} | {var_type} | {var}' + '\n<<<'
        print(out_str)

    else:
        out_str = f'{var_name} | {var_type} | '
        print(out_str)

        if var_type == 'Tensor':
            var_device = var.device
            out_str += f'{var_device} | '

        var_shape = [*(var.shape)]
        out_str += f'{var_shape} '

        try:
            var_max = float(var.max())
            var_min = float(var.min())
            var_mean = float(var.mean())
            var_std = float(var.std())

            out_str += f'| max:{var_max:.2e} | ' + \
                f'min:{var_min:.2e} | mean:{var_mean:.2e} | ' + \
                    f'std:{var_std:.2e} '
        except:
            pass

    out_str = '>>>\n' + out_str + '\n<<<'
    print(out_str)

    return out_str

    