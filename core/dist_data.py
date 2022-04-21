from datetime import datetime
from enum import Enum

from scipy import stats
from numpy import asarray, save, load
import math as math

class distribution_Type( Enum ):
    continuous = 1
    discrete   = 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 


def get_distribution_type( dist ):

    if hasattr( dist, 'dist' ):
        if isinstance( dist.dist, stats.rv_continuous ):
            return distribution_Type.continuous
        else:
            return distribution_Type.discrete

    if isinstance( dist, stats.rv_continuous ):
        return distribution_Type.continuous
    else:
        return distribution_Type.discrete


class Distribution:
    def __init__( 
        self, 
        name, 
        default_args, 
        dist,
        batch_size = 10000
    ) -> None:
        self.name  = name
        self.type  = get_distribution_type( dist )
        self.dist  = dist
        self.p     = set( filter( lambda key: key != "loc" and key != "scale", default_args.keys() ) )
        self.index = -1
        self.default_args = default_args
        self.batch_size   = batch_size
        self.default_args[ "size" ] = batch_size

        # simple performance tests
        # start = datetime.now()

        # asarray( dist.rvs( **self.default_args ) )

        # end = datetime.now()

        # diff = end - start
        # secs = diff.total_seconds()
        # print( f"({name}) Random Numbers per Second: {(self.batch_size / secs):,}" )

    def _rvs( self ) -> None:
        self._random_numbers = self.dist.rvs( **self.default_args )
        self.index = -1

    def rvs( self ):
        if self.index < self.batch_size:
            self.index += 1
            return self._random_numbers[ self.index ]
        else:
            self._rvs()
            return self.random_number()
    
    def get_name( self ):
        return self.name + ""

    def get_params( self ):
        return self.p

    def get_type( self ):
        return self.type



# distributions to check, shape constants were taken from the examples on the scipy.stats 
# distribution documentation pages.

_DISTS = [
        # 24,539,275 / second
        Distribution(
            name = "alpha",
            default_args = { "a": 3.57, "loc": 0.0, "scale": 1.0 },
            dist = stats.alpha
        ), 
        # 32,653,061 / second
        Distribution(
            name = "anglit",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.anglit

        ),  
        # 49,118,326 / second
        Distribution(
            name = "arcsine",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.arcsine

        ), 
        # 8,232,214 / second
        Distribution(
            name = "beta",
            default_args = { "a": 2.31, "b": 0.627, "loc": 0.0, "scale": 1.0 },
            dist = stats.beta

        ), 
        # 10,639,429 / second
        Distribution(
            name = "betaprime",
            default_args = { "a": 5, "b": 6, "loc": 0.0, "scale": 1.0 },
            dist = stats.betaprime

        ), 
        # 49,333,991 / second
        Distribution(
            name = "bradford",
            default_args = { "c": 0.299, "loc": 0.0, "scale": 1.0 },
            dist = stats.bradford

        ), 
        # 13,960,631 / second
        Distribution(
            name = "burr",
            default_args = { "c": 10.5, "d": 4.3, "loc": 0.0, "scale": 1.0 },
            dist = stats.burr

        ), 
        # 27,923,601 / second
        Distribution(
            name = "cauchy",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.cauchy

        ), 
        # 21,922,132 / second
        Distribution(
            name = "chi",
            default_args = { "df": 78, "loc": 0.0, "scale": 1.0 },
            dist = stats.chi

        ), 
        # 20,388,191 / second
        Distribution(
            name = "chi2",
            default_args = { "df": 55, "loc": 0.0, "scale": 1.0 },
            dist = stats.chi2

        ), 
        # 18,753,281 / second
        Distribution(
            name = "cosine",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.cosine

        ), 
        # 16,909,601 / second
        Distribution(
            name = "dgamma",
            default_args = { "a": 1.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.dgamma

        ), 
        # 13,558,770 / second
        Distribution(
            name = "dweibull",
            default_args = { "c": 2.07, "loc": 0.0, "scale": 1.0 },
            dist = stats.dweibull

        ), 
        # 19,514,098 / second
        Distribution(
            name = "erlang",
            default_args = { "a": 2, "loc": 0.0, "scale": 1.0 },
            dist = stats.erlang

        ), 
        # 54,737,533 / second
        Distribution(
            name = "expon",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.expon

        ), 
        # 23,342,670 / second
        Distribution(
            name = "exponnorm",
            default_args = { "K": 1.5, "loc": 0.0, "scale": 1.0 },
            dist = stats.exponnorm

        ), 
        # 12,541,858 / second
        Distribution(
            name = "exponweib",
            default_args = { "a": 2.89, "c": 1.95, "loc": 0.0, "scale": 1.0 },
            dist = stats.exponweib

        ), 
        # 15,797,039 / second
        Distribution(
            name = "exponpow",
            default_args = { "b": 2.7, "loc": 0.0, "scale": 1.0 },
            dist = stats.exponpow,

        ), 
        # 14,015,809 / second
        Distribution(
            name = "f",
            default_args = { "dfn": 29, "dfd": 18, "loc": 0.0, "scale": 1.0 },
            dist = stats.f

        ), 
        # 24,493,594 / second
        Distribution(
            name = "fatiguelife",
            default_args = { "c": 29, "loc": 0.0, "scale": 1.0 },
            dist = stats.fatiguelife

        ), 
        # 20,349,192 / second
        Distribution(
            name = "fisk",
            default_args = { "c": 3.09, "loc": 0.0, "scale": 1.0 },
            dist = stats.fisk

        ), 
        # 30,569,821 / second
        Distribution(
            name = "foldcauchy",
            default_args = { "c": 4.72, "loc": 0.0, "scale": 1.0 },
            dist = stats.foldcauchy

        ), 
        # 32,561,622 / second
        Distribution(
            name = "foldnorm",
            default_args = { "c": 1.95, "loc": 0.0, "scale": 1.0 },
            dist = stats.foldnorm

        ), 
        # 19,604,383 / second
        Distribution(
            name = "genlogistic",
            default_args = { "c": 0.412, "loc": 0.0, "scale": 1.0 },
            dist = stats.genlogistic

        ), 
        # 32,449,621 / second
        Distribution(
            name = "genpareto",
            default_args = { "c": 0.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.genpareto

        ), 
        # 345,303 / second
        # This may be too slow...
        Distribution(
            name = "gennorm",
            default_args = { "beta": 1.3, "loc": 0.0, "scale": 1.0 },
            dist = stats.gennorm

        ), 

        # Too Slow
        # Distribution_Generator(
        #     name = "genexpon",
        #     default_args = { "a": 9.13, "b": 16.2, "c": 3.28, "loc": 0.0, "scale": 1.0 },
        #     dist = stats.genexpon

        # ), 

        # 18,728,696 / second
        Distribution(
            name = "genextreme",
            default_args = { "c": -0.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.genextreme

        ), 
        # 390 / second
        Distribution(
            name = "gausshyper",
            default_args = { "a": 13.8, "b": 3.12, "c": 2.51, "z": 5.18, "loc": 0.0, "scale": 1.0 },
            dist = stats.gausshyper

        ), 
        # 20,570,206 / second
        Distribution(
            name = "gamma",
            default_args = { "a": 1.99, "loc": 0.0, "scale": 1.0 },
            dist = stats.gamma

        ), 
        # 23,334,500 / second
        Distribution(
            name = "gengamma",
            default_args = { "a": 4.42, "loc": 0.0, "scale": 1.0 },
            dist = stats.gamma

        ), 
        # 24,711,493 / second
        Distribution(
            name = "genhalflogistic",
            default_args = { "c": 0.773, "loc": 0.0, "scale": 1.0 },
            dist = stats.genhalflogistic

        ), 
        # 32,997,855 / second
        Distribution(
            name = "gilbrat",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.gilbrat

        ), 
        # 24,696,846 / second
        Distribution(
            name = "gompertz",
            default_args = { "c": 0.947, "loc": 0.0, "scale": 1.0 },
            dist = stats.gompertz

        ), 
        # 32,941,331 / second
        Distribution(
            name = "gumbel_r",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.gumbel_r

        ), 
        # 32,985,882 / second
        Distribution(
            name = "gumbel_l",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.gumbel_l

        ), 
        # 35,250,987 / second
        Distribution(
            name = "halfcauchy",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.halfcauchy

        ), 
        # 44,865,180 / second
        Distribution(
            name = "halflogistic",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.halflogistic

        ), 
        # 33,014,196 / second
        Distribution(
            name = "halfnorm",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.halfnorm
        ), 
        # 2,885,578 / second
        Distribution(
            name = "halfgennorm",
            default_args = { "loc": 0.0, "scale": 1.0, "beta": 1.0 },
            dist = stats.halfgennorm

        ), 
        # 26,018,629 / second
        Distribution(
            name = "hypsecant",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.hypsecant

        ), 
        # 1,706,376 / second
        Distribution(
            name = "invgamma",
            default_args = { "a": 4.07, "loc": 0.0, "scale": 1.0 },
            dist = stats.invgamma

        ), 
        # 23,561,011 / second
        Distribution(
            name = "invgauss",
            default_args = { "mu": 0.145, "loc": 0.0, "scale": 1.0 },
            dist = stats.invgauss

        ), 
        # 19,767,533 / second
        Distribution(
            name = "invweibull",
            default_args = { "c": 10.6, "loc": 0.0, "scale": 1.0 },
            dist = stats.invweibull

        ), 
        # 24,719,434 / second
        Distribution(
            name = "johnsonsb",
            default_args = { "a": 4.32, "b": 3.18, "loc": 0.0, "scale": 1.0 },
            dist = stats.johnsonsb

        ), 
        # 19,787,873 / second
        Distribution(
            name = "johnsonsu",
            default_args = { "a": 2.25, "b": 2.25, "loc": 0.0, "scale": 1.0 },
            dist = stats.johnsonsu

        ),

        # Too Slow
        # Distribution_Generator(
        #     name = "ksone",
        #     default_args = { "n": 1e+03, "loc": 0.0, "scale": 1.0 },
        #     dist = stats.ksone

        # ), 

        # 3,159,487 / second
        Distribution(
            name = "kstwobign",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.kstwobign

        ), 
        # 49,404,673 / second
        Distribution(
            name = "laplace",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.laplace

        ), 
        # 24,688,310 / second
        Distribution(
            name = "levy",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.levy

        ), 
        # 26,001,040 / second
        Distribution(
            name = "levy_l",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.levy_l

        ), 
        # 3,629,144 / second
        Distribution(
            name = "levy_stable",
            default_args = { "alpha": 0.357, "beta": -0.675, "loc": 0.0, "scale": 1.0 },
            dist = stats.levy_stable

        ), 
        # 49,341,293 / second
        Distribution(
            name = "logistic",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.logistic

        ), 
        # 12,351,626 / second
        Distribution(
            name = "loggamma",
            default_args = { "c": 0.414, "loc": 0.0, "scale": 1.0 },
            dist = stats.loggamma

        ), 
        # 14,111,537 / second
        Distribution(
            name = "loglaplace",
            default_args = { "c": 3.25, "loc": 0.0, "scale": 1.0 },
            dist = stats.loglaplace

        ), 
        # 32,927,230 / second
        Distribution(
            name = "lognorm",
            default_args = { "s": 0.954, "loc": 0.0, "scale": 1.0 },
            dist = stats.lognorm

        ), 
        # 24,677,343 / second
        Distribution(
            name = "lomax",
            default_args = { "c": 1.88, "loc": 0.0, "scale": 1.0 },
            dist = stats.lomax

        ), 
        # 19,719,976 / second
        Distribution(
            name = "maxwell",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.maxwell

        ), 
        # 49,465,769/ second
        Distribution(
            name = "mielke",
            default_args = { "loc": 0.0, "scale": 1.0, "k": 1.0, "s": 1.0 },
            dist = stats.mielke

        ), 
        # 1,706,417 / second
        Distribution(
            name = "nakagami",
            default_args = { "nu": 4.97, "loc": 0.0, "scale": 1.0 },
            dist = stats.nakagami

        ), 
        # 14,117,115 / second
        Distribution(
            name = "ncx2",
            default_args = { "df": 21, "nc": 1.06, "loc": 0.0, "scale": 1.0 },
            dist = stats.ncx2

        ), 
        # 9,891,392 / second
        Distribution(
            name = "ncf",
            default_args = { "dfn": 27, "dfd": 27, "nc": 0.416, "loc": 0.0, "scale": 1.0 },
            dist = stats.ncf

        ), 
        # 12,660,631 / second
        Distribution(
            name = "nct",
            default_args = { "df": 14, "nc": 0.24, "loc": 0.0, "scale": 1.0 },
            dist = stats.nct

        ), 
        # 44,686,745 / second
        Distribution(
            name = "norm",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.norm

        ), 

        # 24,694,406 / second
        Distribution(
            name = "pareto",
            default_args = { "b": 2.62, "loc": 0.0, "scale": 1.0 },
            dist = stats.pareto

        ), 
        # 12,346,593 / second
        Distribution(
            name = "pearson3",
            default_args = { "skew": 0.1, "loc": 0.0, "scale": 1.0 },
            dist = stats.pearson3

        ), 
        # 25,996,308 / second
        Distribution(
            name = "powerlaw",
            default_args = { "a": 1.66, "loc": 0.0, "scale": 1.0 },
            dist = stats.powerlaw

        ), 
        # 15,918,497 / second
        Distribution(
            name = "powerlognorm",
            default_args = { "c": 2.14, "s": 0.446, "loc": 0.0, "scale": 1.0 },
            dist = stats.powerlognorm

        ), 
        # 16,464,970 / second
        Distribution(
            name = "powernorm",
            default_args = { "c": 4.45, "loc": 0.0, "scale": 1.0 },
            dist = stats.powernorm

        ), 
        # 9,884,548 / second
        Distribution(
            name = "r",
            default_args = { "c": 0.9, "loc": 0.0, "scale": 1.0 },
            dist = stats.rdist

        ), 
        # 24,648,755 / second
        Distribution(
            name = "reciprocal",
            default_args = { "a": 0.00623, "b": 1.01, "loc": 0.0, "scale": 1.0 },
            dist = stats.reciprocal

        ), 
        # 32,853,669 / second
        Distribution(
            name = "rayleigh",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.rayleigh

        ), 
        # 19,784,742 / second
        Distribution(
            name = "rice",
            default_args = { "b": 0.775, "loc": 0.0, "scale": 1.0 },
            dist = stats.rice

        ), 
        # 19,705,986 / second
        Distribution(
            name = "recipinvgauss",
            default_args = { "mu": 0.63, "loc": 0.0, "scale": 1.0 },
            dist = stats.recipinvgauss

        ), 
        # 26,009,831 / second
        Distribution(
            name = "semicircular",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.semicircular

        ), 
        # 15,936,508 / second
        Distribution(
            name = "t",
            default_args = { "df": 2.74, "loc": 0.0, "scale": 1.0 },
            dist = stats.t

        ), 
        # 49,536,830 / second
        Distribution(
            name = "triang",
            default_args = { "c": 0.158, "loc": 0.0, "scale": 1.0 },
            dist = stats.triang

        ), 
        # 35,380,696 / second
        Distribution(
            name = "truncexpon",
            default_args = { "b": 4.69, "loc": 0.0, "scale": 1.0 },
            dist = stats.truncexpon

        ), 
        # 23,479,690 / second
        Distribution(
            name = "truncnorm",
            default_args = { "a": 0.1, "b": 2, "loc": 0.0, "scale": 1.0 },
            dist = stats.truncnorm

        ), 
        # 16,464,428 / second
        Distribution(
            name = "tukeylambda",
            default_args = { "lam": 3.13, "loc": 0.0, "scale": 1.0 },
            dist = stats.tukeylambda

        ), 
        # 98,619,329 / second
        Distribution(
            name = "uniform",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.uniform

        ), 
        # 10,998,317 / second
        Distribution(
            name = "vonmises",
            default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },
            dist = stats.vonmises

        ), 
        # 10,990,943 / second
        Distribution(
            name = "vonmises_line",
            default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },
            dist = stats.vonmises_line

        ), 
        # 24,733,496 / second
        Distribution(
            name = "wald",
            default_args = { "loc": 0.0, "scale": 1.0 },
            dist = stats.wald

        ), 
        # 19,783,959 / second
        Distribution(
            name = "weibull_min",
            default_args = { "c":1.79, "loc": 0.0, "scale": 1.0 },
            dist = stats.weibull_min

        ), 
        # 19,739,049 / second
        Distribution(
            name = "weibull_max",
            default_args = { "c":2.87, "loc": 0.0, "scale": 1.0 },
            dist = stats.weibull_max

        ), 
        # 12,348,880 / second
        Distribution(
            name = "wrapcauchy",
            default_args = { "c":0.0311, "loc": 0.0, "scale": 1.0 },
            dist = stats.wrapcauchy
        )
]

DISTRIBUTIONS = { d.get_name(): d for d in _DISTS }
# print( DISTRIBUTIONS[ "alpha" ].get_type() )

def is_distribution( dist, check_dist ):
    if not isinstance( dist, Distribution ):
        raise ValueError( "dist must be an instance of the Distribution class" )
        
    return dist.get_name() == check_dist

# This assumes that supported_dists are also in the DISTS list
def valid_distribution( dist, supported_dists ):
    if not isinstance( dist, Distribution ):
        raise ValueError( "dist must be an instance of the Distribution class" )
    
    return dist.get_name() in supported_dists


def get_distribution( name ):
    if not ( isinstance( name, str ) and name != "" ):
        raise ValueError( "name must be a string" )
    
    # ability to add custom error message here when ready
    if not DISTRIBUTIONS.has_key( name ):
        raise ValueError( f"{name} is not a supported distribution" )

    return DISTRIBUTIONS.get( name )