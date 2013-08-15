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

def vector_p(collection): 
	if collection == 'SmoothReflexive':
		return [
			'CENTROID',
			'FACET_WIDTHS',
			'F_VECTOR',
			'H_STAR_VECTOR',
			'EHRHART_POLYNOMIAL_COEFF'
		]

def matrix_p(collection):
	if collection == 'SmoothReflexive':
		return [
			'VERTICES',
			'FACETS'
		]
		