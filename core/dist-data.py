from enum import Enum
from importlib.metadata import distributions

from scipy import stats
import numpy as np
import math as math

class Distribution_Type( Enum ):
    continuos = 1
    discrete  = 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_ 



class Distribution:
    def __init__( self, name, default_args, dist, link, dist_type = Distribution_Type.continuos ) -> None:
        if not isinstance( dist_type, Distribution_Type ):
            raise ValueError( "dist_type must be Distribution_Type.continuos or Distribution_Type.discrete" )

        self.name = name
        self.default_args = default_args
        self.type = dist_type
        self.dist = dist
        self.link = link
        self.params = list( filter( lambda key: key != "loc" and key != "scale", default_args.keys() ) )



# Distributions to check, shape constants were taken from the examples on the scipy.stats distribution documentation pages.
DISTRIBUTIONS = [
    Distribution( 
        name = "alpha",           
        default_args = { "a": 3.57, "loc": 0.0, "scale": 1.0 },
        dist = stats.alpha,
        link = "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.alpha.html" 
    ), 
    Distribution( 
        name = "anglit",
        default_args = { "loc": 0.0, "scale": 1.0 },
        dist = stats.anglit,
        link = "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anglit.html" 
    ), 
    Distribution( 
        name = "arcsine",
        default_args = { "loc": 0.0, "scale": 1.0 },
        dist = stats.arcsine,
        link = "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.arcsine.html" 
    ), 
    Distribution( name = "beta",            default_args = { "a": 2.31, "b": 0.627, "loc": 0.0, "scale": 1.0 },                      dist = stats.beta,            link = "" ), 
    Distribution( name = "betaprime",       default_args = { "a": 5, "b": 6, "loc": 0.0, "scale": 1.0 },                             dist = stats.betaprime,       link = "" ), 
    Distribution( name = "bradford",        default_args = { "c": 0.299, "loc": 0.0, "scale": 1.0 },                                 dist = stats.bradford,        link = "" ), 
    Distribution( name = "burr",            default_args = { "c": 10.5, "d": 4.3, "loc": 0.0, "scale": 1.0 },                        dist = stats.burr,            link = "" ), 
    Distribution( name = "cauchy",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.cauchy,          link = "" ), 
    Distribution( name = "chi",             default_args = { "df": 78, "loc": 0.0, "scale": 1.0 },                                   dist = stats.chi,             link = "" ), 
    Distribution( name = "chi2",            default_args = { "df": 55, "loc": 0.0, "scale": 1.0 },                                   dist = stats.chi2,            link = "" ), 
    Distribution( name = "cosine",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.cosine,          link = "" ), 
    Distribution( name = "dgamma",          default_args = { "a": 1.1, "loc": 0.0, "scale": 1.0 },                                   dist = stats.dgamma,          link = "" ), 
    Distribution( name = "dweibull",        default_args = { "c": 2.07, "loc": 0.0, "scale": 1.0 },                                  dist = stats.dweibull,        link = "" ), 
    Distribution( name = "erlang",          default_args = { "a": 2, "loc": 0.0, "scale": 1.0 },                                     dist = stats.erlang,          link = "" ), 
    Distribution( name = "expon",           default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.expon,           link = "" ), 
    Distribution( name = "expon",           default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.expon,           link = "" ), 
    Distribution( name = "exponnorm",       default_args = { "K": 1.5, "loc": 0.0, "scale": 1.0 },                                   dist = stats.exponnorm,       link = "" ), 
    Distribution( name = "exponweib",       default_args = { "a": 2.89, "c": 1.95, "loc": 0.0, "scale": 1.0 },                       dist = stats.exponweib,       link = "" ), 
    Distribution( name = "exponpow",        default_args = { "b": 2.7, "loc": 0.0, "scale": 1.0 },                                   dist = stats.exponpow,        link = "" ), 
    Distribution( name = "f",               default_args = { "dfn": 29, "dfd": 18, "loc": 0.0, "scale": 1.0 },                       dist = stats.f,               link = "" ), 
    Distribution( name = "fatiguelife",     default_args = { "c": 29, "loc": 0.0, "scale": 1.0 },                                    dist = stats.fatiguelife,     link = "" ), 
    Distribution( name = "fisk",            default_args = { "c": 3.09, "loc": 0.0, "scale": 1.0 },                                  dist = stats.fisk,            link = "" ), 
    Distribution( name = "foldcauchy",      default_args = { "c": 4.72, "loc": 0.0, "scale": 1.0 },                                  dist = stats.foldcauchy,      link = "" ), 
    Distribution( name = "foldnorm",        default_args = { "c": 1.95, "loc": 0.0, "scale": 1.0 },                                  dist = stats.foldnorm,        link = "" ), 
    Distribution( name = "genlogistic",     default_args = { "c": 0.412, "loc": 0.0, "scale": 1.0 },                                 dist = stats.genlogistic,     link = "" ), 
    Distribution( name = "genpareto",       default_args = { "c": 0.1, "loc": 0.0, "scale": 1.0 },                                   dist = stats.genpareto,       link = "" ), 
    Distribution( name = "genpareto",       default_args = { "c": 0.1, "loc": 0.0, "scale": 1.0 },                                   dist = stats.genpareto,       link = "" ), 
    Distribution( name = "gennorm",         default_args = { "beta": 1.3, "loc": 0.0, "scale": 1.0 },                                dist = stats.gennorm,         link = "" ), 
    Distribution( name = "genexpon",        default_args = { "a": 9.13, "b": 16.2, "c": 3.28, "loc": 0.0, "scale": 1.0 },            dist = stats.genexpon,        link = "" ), 
    Distribution( name = "genextreme",      default_args = { "c": -0.1, "loc": 0.0, "scale": 1.0 },                                  dist = stats.genextreme,      link = "" ), 
    Distribution( name = "gausshyper",      default_args = { "a": 13.8, "b": 3.12, "c": 2.51, "z": 5.18, "loc": 0.0, "scale": 1.0 }, dist = stats.gausshyper,      link = "" ), 
    Distribution( name = "gamma",           default_args = { "a": 1.99, "loc": 0.0, "scale": 1.0 },                                  dist = stats.gamma,           link = "" ), 
    Distribution( name = "gengamma",        default_args = { "a": 4.42, "c": -3.12, "loc": 0.0, "scale": 1.0 },                      dist = stats.gamma,           link = "" ), 
    Distribution( name = "genhalflogistic", default_args = { "c": 0.773, "loc": 0.0, "scale": 1.0 },                                 dist = stats.genhalflogistic, link = "" ), 
    Distribution( name = "gilbrat",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.gilbrat,         link = "" ), 
    Distribution( name = "gompertz",        default_args = { "c": 0.947, "loc": 0.0, "scale": 1.0 },                                 dist = stats.gompertz,        link = "" ), 
    Distribution( name = "gumbel_r",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.gumbel_r,        link = "" ), 
    Distribution( name = "gumbel_l",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.gumbel_l,        link = "" ), 
    Distribution( name = "halfcauchy",      default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halfcauchy,      link = "" ), 
    Distribution( name = "halflogistic",    default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halflogistic,    link = "" ), 
    Distribution( name = "halfnorm",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halfnorm,        link = "" ), 
    Distribution( name = "halfgennorm",     default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.halfgennorm,     link = "" ), 
    Distribution( name = "hypsecant",       default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.hypsecant,       link = "" ), 
    Distribution( name = "invgamma",        default_args = { "a": 4.07, "loc": 0.0, "scale": 1.0 },                                  dist = stats.invgamma,        link = "" ), 
    Distribution( name = "invgauss",        default_args = { "mu": 0.145, "loc": 0.0, "scale": 1.0 },                                dist = stats.invgauss,        link = "" ), 
    Distribution( name = "invweibull",      default_args = { "c": 10.6, "loc": 0.0, "scale": 1.0 },                                  dist = stats.invweibull,      link = "" ), 
    Distribution( name = "johnsonsb",       default_args = { "a": 4.32, "b": 3.18, "loc": 0.0, "scale": 1.0 },                       dist = stats.johnsonsb,       link = "" ), 
    Distribution( name = "johnsonsu",       default_args = { "a": 2.25, "b": 2.25, "loc": 0.0, "scale": 1.0 },                       dist = stats.johnsonsu,       link = "" ), 
    Distribution( name = "ksone",           default_args = { "n": 1e+03, "loc": 0.0, "scale": 1.0 },                                 dist = stats.ksone,           link = "" ), 
    Distribution( name = "kstwobign",       default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.kstwobign,       link = "" ), 
    Distribution( name = "laplace",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.laplace,         link = "" ), 
    Distribution( name = "levy",            default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.levy,            link = "" ), 
    Distribution( name = "levy_l",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.levy_l,          link = "" ), 
    Distribution( name = "levy_stable",     default_args = { "alpha": 0.357, "beta": -0.675, "loc": 0.0, "scale": 1.0 },             dist = stats.levy_stable,     link = "" ), 
    Distribution( name = "logistic",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.logistic,        link = "" ), 
    Distribution( name = "loggamma",        default_args = { "c": 0.414, "loc": 0.0, "scale": 1.0 },                                 dist = stats.loggamma,        link = "" ), 
    Distribution( name = "loglaplace",      default_args = { "c": 3.25, "loc": 0.0, "scale": 1.0 },                                  dist = stats.loglaplace,      link = "" ), 
    Distribution( name = "lognorm",         default_args = { "s": 0.954, "loc": 0.0, "scale": 1.0 },                                 dist = stats.lognorm,         link = "" ), 
    Distribution( name = "lomax",           default_args = { "c": 1.88, "loc": 0.0, "scale": 1.0 },                                  dist = stats.lomax,           link = "" ), 
    Distribution( name = "maxwell",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.maxwell,         link = "" ), 
    Distribution( name = "mielke",          default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.mielke,          link = "" ), 
    Distribution( name = "nakagami",        default_args = { "nu": 4.97, "loc": 0.0, "scale": 1.0 },                                 dist = stats.nakagami,        link = "" ), 
    Distribution( name = "ncx2",            default_args = { "df": 21, "nc": 1.06, "loc": 0.0, "scale": 1.0 },                       dist = stats.ncx2,            link = "" ), 
    Distribution( name = "ncf",             default_args = { "dfn": 27, "dfd": 27, "nc": 0.416, "loc": 0.0, "scale": 1.0 },          dist = stats.ncf,             link = "" ), 
    Distribution( name = "nct",             default_args = { "df": 14, "nc": 0.24, "loc": 0.0, "scale": 1.0 },                       dist = stats.nct,             link = "" ), 
    Distribution( name = "norm",            default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.norm,            link = "" ), 
    Distribution( name = "pareto",          default_args = { "b": 2.62, "loc": 0.0, "scale": 1.0 },                                  dist = stats.pareto,          link = "" ), 
    Distribution( name = "pearson3",        default_args = { "skew": 0.1, "loc": 0.0, "scale": 1.0 },                                dist = stats.pearson3,        link = "" ), 
    Distribution( name = "powerlaw",        default_args = { "a": 1.66, "loc": 0.0, "scale": 1.0 },                                  dist = stats.powerlaw,        link = "" ), 
    Distribution( name = "powerlognorm",    default_args = { "c": 2.14, "s": 0.446, "loc": 0.0, "scale": 1.0 },                      dist = stats.powerlognorm,    link = "" ), 
    Distribution( name = "powernorm",       default_args = { "c": 4.45, "loc": 0.0, "scale": 1.0 },                                  dist = stats.powernorm,       link = "" ), 
    Distribution( name = "rdist",           default_args = { "c": 0.9, "loc": 0.0, "scale": 1.0 },                                   dist = stats.rdist,           link = "" ), 
    Distribution( name = "reciprocal",      default_args = { "a": 0.00623, "b": 1.01, "loc": 0.0, "scale": 1.0 },                    dist = stats.reciprocal,      link = "" ), 
    Distribution( name = "rayleigh",        default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.rayleigh,        link = "" ), 
    Distribution( name = "rice",            default_args = { "b": 0.775, "loc": 0.0, "scale": 1.0 },                                 dist = stats.rice,            link = "" ), 
    Distribution( name = "recipinvgauss",   default_args = { "mu": 0.63, "loc": 0.0, "scale": 1.0 },                                 dist = stats.recipinvgauss,   link = "" ), 
    Distribution( name = "semicircular",    default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.semicircular,    link = "" ), 
    Distribution( name = "t",               default_args = { "df": 2.74, "loc": 0.0, "scale": 1.0 },                                 dist = stats.t,               link = "" ), 
    Distribution( name = "triang",          default_args = { "c": 0.158, "loc": 0.0, "scale": 1.0 },                                 dist = stats.triang,          link = "" ), 
    Distribution( name = "truncexpon",      default_args = { "b": 4.69, "loc": 0.0, "scale": 1.0 },                                  dist = stats.truncexpon,      link = "" ), 
    Distribution( name = "truncnorm",       default_args = { "a": 0.1, "b": 2, "loc": 0.0, "scale": 1.0 },                           dist = stats.truncnorm,       link = "" ), 
    Distribution( name = "tukeylambda",     default_args = { "lam": 3.13, "b": 2, "loc": 0.0, "scale": 1.0 },                        dist = stats.tukeylambda,     link = "" ), 
    Distribution( name = "tukeylambda",     default_args = { "lam": 3.13, "loc": 0.0, "scale": 1.0 },                                dist = stats.tukeylambda,     link = "" ), 
    Distribution( name = "uniform",         default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.uniform,         link = "" ), 
    Distribution( name = "vonmises",        default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },                               dist = stats.vonmises,        link = "" ), 
    Distribution( name = "vonmises_line",   default_args = { "kappa":3.99, "loc": 0.0, "scale": 1.0 },                               dist = stats.vonmises_line,   link = "" ), 
    Distribution( name = "wald",            default_args = { "loc": 0.0, "scale": 1.0 },                                             dist = stats.wald,            link = "" ), 
    Distribution( name = "weibull_min",     default_args = { "c":1.79, "loc": 0.0, "scale": 1.0 },                                   dist = stats.weibull_min,     link = "" ), 
    Distribution( name = "weibull_max",     default_args = { "c":2.87, "loc": 0.0, "scale": 1.0 },                                   dist = stats.weibull_max,     link = "" ), 
    Distribution( name = "wrapcauchy",      default_args = { "c":0.0311, "loc": 0.0, "scale": 1.0 },                                 dist = stats.wrapcauchy,      link = "" )
]


print( DISTRIBUTIONS[0].params )