# --- Pack/Unpack ---

def morloc_packMap(xs):
    return dict(xs)

def morloc_unpackMap(d):
    return list(d.items())

# --- Construction ---

def morloc_emptyMap():
    return {}

def morloc_singleton(k, v):
    return {k: v}

def morloc_from_list(xs):
    return dict(xs)

def morloc_to_list(m):
    return list(m.items())

# --- Query ---

def morloc_lookup(key, m):
    return m[key]

def morloc_member(key, m):
    return key in m

def morloc_size(m):
    return len(m)

# --- Modify ---

def morloc_insert(key, val, m):
    result = dict(m)
    result[key] = val
    return result

def morloc_delete(key, m):
    result = dict(m)
    result.pop(key, None)
    return result

# --- Bulk access ---

def morloc_keys(d):
    return list(d.keys())

def morloc_vals(d):
    return list(d.values())

# --- Combine ---

def morloc_union(a, b):
    return {**a, **b}

def morloc_unionWith(f, a, b):
    result = dict(a)
    for k, v in b.items():
        if k in result:
            result[k] = f(result[k], v)
        else:
            result[k] = v
    return result

def morloc_intersectionWith(f, a, b):
    result = {}
    for k, v in a.items():
        if k in b:
            result[k] = f(v, b[k])
    return result

def morloc_difference(a, b):
    return {k: v for k, v in a.items() if k not in b}

# --- Transform ---

def morloc_map_val(f, m):
    return {k: f(v) for k, v in m.items()}

def morloc_map_key(f, m):
    return {f(k): v for k, v in m.items()}

def morloc_mapWithKey(f, m):
    return {k: f(k, v) for k, v in m.items()}

def morloc_filter_map(f, m):
    return {k: v for k, v in m.items() if f(k, v)}

def morloc_foldWithKey(f, init, m):
    acc = init
    for k, v in m.items():
        acc = f(acc, k, v)
    return acc
