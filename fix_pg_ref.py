import re
from pathlib import Path

def get_pages(poti_text):
    result = []
    pg_text = ""
    pages = re.split(r"(Page no.+)", poti_text)
    for i, page in enumerate(pages[1:]):
        if i % 2 == 0:
            pg_text += page
        else:
            pg_text += page
            result.append(pg_text)
            pg_text = ""
    return result

def add_pg_ref(poti_text, poti_img_grp):
    pages = get_pages(poti_text)
    new_poti_text = f'{poti_img_grp}\n\n'
    for page_walker, page in enumerate(pages):
        pg_id = f'{poti_img_grp[1:]}_{page_walker:04}'
        new_poti_text += re.sub('Page no.+', f'Page no:{pg_id}', page)
    return new_poti_text
    


if __name__ == "__main__":
    poti_paths = list(Path('./transcript/').iterdir())
    poti_paths.sort()
    for poti_path in poti_paths[39:120]:
        poti_text = poti_path.read_text(encoding='utf-8')
        poti_img_grp = poti_path.stem
        new_poti_text = add_pg_ref(poti_text, poti_img_grp)
        Path(f'./with_pg_ref/{poti_img_grp}.txt').write_text(new_poti_text, encoding='utf-8')
        print(f'{poti_img_grp} completed...')
