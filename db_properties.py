def simple_p(collection): 
	if collection == 'SmoothReflexive':
		return [
			'CONE_DIM', 
			'N_VERTICES', 
			'N_FACETS'
			'FACET_WIDTH',
			'LATTICE_VOLUME',
			'N_INTERIOR_LATTICE_POINTS',
			'N_BOUNDARY_LATTICE_POINTS',
			'N_LATTICE_POINTS',
			'ESSENTIALLY_GENERIC',
			'GORENSTEIN',
			'LATTICE_CODEGREE',
			'LATTICE_DEGREE',
			'REFLEXIVE',
			'SMOOTH',
			'VERY_AMPLE'
		]
		# indices: cone_dim, n_vertices, n_facets, lattice_volume, n_lattice_points, lattice_codegree, lattice_degree
	elif collection == 'TOM':
		return [
			'N_PHP',
			'RANK',
			'DIM',
			'N_VERTICES',
			'N_TOPES',
			'N_TYPES',
			'N_APICES'
			'GENERAL_POSITION',
			'BOUNDARY_AXIOM',
			'SURROUNDING_AXIOM',
			'COMPARABILITY_AXIOM',
			'ELIMINATION_AXIOM',
			'IS_TOM',
		]


def vector_p(collection): 
	if collection == 'SmoothReflexive':
		return [
			'CENTROID',
			'FACET_WIDTHS',
			'F_VECTOR',
			'H_STAR_VECTOR',
			'EHRHART_POLYNOMIAL_COEFF'
		]
	elif collection == 'TOM':
		return []
		

def matrix_p(collection):
	if collection == 'SmoothReflexive':
		return [
			'VERTICES',
			'FACETS'
		]
	elif collection == 'TOM':
		return []


def mmatrix_p(collection):
	if collection == 'SmoothReflexive':
		return []
	elif collection == 'TOM':
		return [
			'VERTICES',
			'TOPES',
			'APICES'
		]