import xml.etree.ElementTree as ET
import re

tree = ET.parse('Sistem_Katalog_UMKM_Gorontalo.drawio')
root = tree.getroot()

for diag in root.findall('diagram'):
    print('======================================================================')
    print('DIAGRAM:', diag.get('name'))
    print('======================================================================')
    model = diag.find('mxGraphModel')
    cells = model.find('root').findall('mxCell')
    
    cell_map = {}
    vertices = []
    edges = []
    
    for c in cells:
        cell_map[c.get('id')] = c
        if c.get('vertex') == '1':
            geo = c.find('mxGeometry')
            if geo is not None:
                x = float(geo.get('x', 0))
                y = float(geo.get('y', 0))
                w = float(geo.get('width', 0))
                h = float(geo.get('height', 0))
                raw_val = c.get('value', '')
                clean_val = re.sub(r'<[^>]+>', ' ', raw_val).strip()
                clean_val = ' '.join(clean_val.split())
                vertices.append({
                    'id': c.get('id'),
                    'name': clean_val[:30],
                    'rect': (x, y, x + w, y + h),
                    'x': x, 'y': y, 'w': w, 'h': h
                })
        elif c.get('edge') == '1':
            edges.append(c)
            
    print(f"Total Vertices: {len(vertices)}, Total Edges: {len(edges)}")
    
    for e in edges:
        src_id = e.get('source')
        tgt_id = e.get('target')
        src_cell = cell_map.get(src_id)
        tgt_cell = cell_map.get(tgt_id)
        src_val = re.sub(r'<[^>]+>', ' ', src_cell.get('value', '')).strip() if src_cell is not None else 'None'
        tgt_val = re.sub(r'<[^>]+>', ' ', tgt_cell.get('value', '')).strip() if tgt_cell is not None else 'None'
        src_clean = ' '.join(src_val.split())[:25]
        tgt_clean = ' '.join(tgt_val.split())[:25]
        
        lbl = re.sub(r'<[^>]+>', ' ', e.get('value', '')).strip()
        lbl = ' '.join(lbl.split())
        
        geo = e.find('mxGeometry')
        pts = []
        if geo is not None:
            arr = geo.find('Array')
            if arr is not None:
                for pt in arr.findall('mxPoint'):
                    pts.append((float(pt.get('x')), float(pt.get('y'))))
                    
        print(f"  Edge [{src_clean}] -> [{tgt_clean}]")
        print(f"       Label: {lbl[:45]}...")
        print(f"       Waypoints: {pts}")
