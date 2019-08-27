import turicreate
loaded_model = turicreate.load_model('./image_model')


def find_image(path):
    print(path)
    img = turicreate.Image(path)
    ary = turicreate.SArray([img])
    results = loaded_model.query(ary, k=1)
    return results['reference_label'][0]
