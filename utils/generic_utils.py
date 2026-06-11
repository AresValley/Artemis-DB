import hashlib
import re


def format_acf(acf_string):
    # Gestione stringa vuota o segnaposto
    if not acf_string or acf_string.strip() in ('—', '', '-'):
        return []
    
    acf_list = []
    
    # Dividiamo per virgola o per la parola "and" per separare i vari token
    tokens = re.split(r',', acf_string)
    
    for token in tokens:
        token = token.strip()
        if not token:
            continue
            
        acf_description = 'Main'
        acf_value = 0.0
        
        # Se ci sono i due punti, separiamo la descrizione dal valore
        if ':' in token:
            parts = token.split(':', 1)
            acf_description = parts[0].strip()
            value_part = parts[1].strip()
        else:
            value_part = token
            
        # Regex per cercare il primo numero (intero o decimale) associato a ms
        # Cattura pattern come: "13.3 ms", "426.66 ms / 512 bits", "150ms"
        match = re.search(r'(\d+(?:\.\d+)?)\s*ms', value_part, re.IGNORECASE)
        
        if match:
            acf_value = float(match.group(1))
        else:
            # Se non trova "ms" con un numero, ma c'è del testo (es. "variable" o "Depending on...")
            # salviamo il testo extra nella descrizione per non perdere l'info
            if acf_description == 'Main':
                acf_description = value_part
            else:
                acf_description = f"{acf_description} ({value_part})"
            acf_value = 0.0
            
        acf_list.append((acf_description, acf_value))
        
    return acf_list


def format_text(raw_string):
    """ Used for modulation, mode and location
    """
    if raw_string == '—':
        list_result = []
    else:
        list_result = raw_string.split(',')
    
    list_result = [x.strip() for x in list_result]

    return list_result


def checksum_sha256(data):
    """ Calculate SHA256 hash
    """
    code  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(data, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            code.update(mv[:n])
            
    return code.hexdigest()
