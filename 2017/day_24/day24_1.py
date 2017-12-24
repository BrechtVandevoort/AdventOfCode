lines = map(lambda x: x.strip().split('/'), open('input.txt').readlines())
components = [[int(a), int(b)] for a, b in lines]

def max_bridge(port, components):
	max_strength = 0
	for i, comp in enumerate(components):
		if port in comp:
			new_port = comp[0] if port == comp[1] else comp[1]
			new_components = components[:i] + components[i+1:]
			strength = max_bridge(new_port, new_components)
			strength += sum(comp)
			max_strength = max(max_strength, strength)
	return max_strength

print max_bridge(0, components)