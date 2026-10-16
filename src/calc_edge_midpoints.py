import xml.etree.ElementTree as ET

tree = ET.parse('Sistem_Katalog_UMKM_Gorontalo.drawio')
root = tree.getroot()

def get_edge_segments(edge, cell_map):
    src = cell_map.get(edge.get('source'))
    tgt = cell_map.get(edge.get('target'))
    if src is None or tgt is None:
        return []
    
    sgeo = src.find('mxGeometry')
    tgeo = tgt.find('mxGeometry')
    
    style = edge.get('style', '')
    
    # parse exit/entry
    exitX = 0.5
    exitY = 0.5
    entryX = 0.5
    entryY = 0.5
    for part in style.split(';'):
        if part.startswith('exitX='): exitX = float(part.split('=')[1])
        if part.startswith('exitY='): exitY = float(part.split('=')[1])
        if part.startswith('entryX='): entryX = float(part.split('=')[1])
        if part.startswith('entryY='): entryY = float(part.split('=')[1])
        
    sx = float(sgeo.get('x', 0)) + float(sgeo.get('width', 0)) * exitX
    sy = float(sgeo.get('y', 0)) + float(sgeo.get('height', 0)) * exitY
    tx = float(tgeo.get('x', 0)) + float(tgeo.get('width', 0)) * entryX
    ty = float(tgeo.get('y', 0)) + float(tgeo.get('height', 0)) * entryY
    
    pts = [(sx, sy)]
    geo = edge.find('mxGeometry')
    if geo is not None:
        arr = geo.find('Array')
        if arr is not None:
            for p in arr.findall('mxPoint'):
                pts.append((float(p.get('x')), float(p.get('y'))))
    pts.append((tx, ty))
    return pts

for diag in root.findall('diagram'):
    name = diag.get('name')
    print(f"\n*** DIAGRAM: {name} ***")
    model = diag.find('mxGraphModel')
    cells = model.find('root').findall('mxCell')
    cell_map = {c.get('id'): c for c in cells}
    
    for c in cells:
        if c.get('edge') == '1':
            lbl = c.get('value', '').replace('\n', ' ')[:40]
            pts = get_edge_segments(c, cell_map)
            # calculate rough midpoint
            total_len = 0
            lens = []
            for i in range(len(pts)-1):
                d = ((pts[i+1][0]-pts[i][0])**2 + (pts[i+1][1]-pts[i][1])**2)**0.5
                lens.append(d)
                total_len += d
            half = total_len / 2
            cur = 0
            mid = pts[0] if pts else (0,0)
            for i in range(len(lens)):
                if cur + lens[i] >= half:
                    rem = half - cur
                    ratio = rem / lens[i] if lens[i] > 0 else 0
                    mid = (pts[i][0] + (pts[i+1][0]-pts[i][0])*ratio, pts[i][1] + (pts[i+1][1]-pts[i][1])*ratio)
                    break
                cur += lens[i]
            print(f"Edge '{lbl}': Midpoint around ({mid[0]:.1f}, {mid[1]:.1f}) | Path: {pts}")
