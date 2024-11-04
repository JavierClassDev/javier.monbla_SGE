def diferencia_annos(anno_dado):
    anno_actual=2024
    dif_anno=anno_dado-anno_actual
    match dif_anno:
        case -1:
            print(f"Desde el año {anno_dado} ha pasado 1 año")
        case 1:
            print(f"Para llegar al año {anno_dado} falta 1 año")
        case 0:
            print("Son el mismo año")
        case _:
            if(dif_anno<1):
                print(f"Desde el año {anno_dado} han pasado {-dif_anno} años")
            if(dif_anno>1):
                print(f"Para llegar al año {anno_dado} faltan {-dif_anno} años")

anno = int(input("El año que desea comparar al actual: "))
diferencia_annos(anno)
